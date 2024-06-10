<template>
  <el-container class="container-bg">
    <el-aside width="400px" class="custom-aside">
      <el-menu :default-active="activeMenuItem" @select="handleMenuSelect">
        <el-menu-item index="overview" class="menu-item" @click="fetchAllBugs(`总览`)"
          >总览</el-menu-item
        >
        <el-sub-menu index="product-components" class="menu-item">
          <template #title>产品组件</template>
          <el-sub-menu
            v-for="product in productComponentTypes"
            :key="product.product"
            :index="`product-components-${product.product}`"
          >
            <template #title>
              {{ product.product }}
            </template>
            <el-menu-item
              v-for="component in product.components"
              :key="component"
              :index="`product-components-${product.product}-${component}`"
              @click="selectProductComponent(product.product, component, `product-components-${product.product}-${component}`)"
              class="menu-item"
            >
              {{ component }}
            </el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-sub-menu index="status" class="menu-item">
          <template #title>状态</template>
          <el-menu-item
            v-for="status in statusTypes"
            :key="status"
            :index="`status-${status}`"
            @click="selectStatus(status, `status-${status}`)"
            class="menu-item"
          >
            {{ status }}
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="platform" class="menu-item">
          <template #title>平台</template>
          <el-menu-item
            v-for="platform in platformTypes"
            :key="platform"
            :index="`platform-${platform}`"
            @click="selectPlatform(platform, `platform-${platform}`)"
            class="menu-item"
          >
            {{ platform }}
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="company" class="menu-item">
          <template #title>公司</template>
          <el-menu-item
            v-for="company in companyTypes"
            :key="company"
            :index="`company-${company}`"
            @click="selectCompany(company, `company-${company}`)"
            class="menu-item"
          >
            {{ company }}
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-main class="custom-main">
      <h3>{{ currentTitle }}</h3>
      <el-divider />
      <div class="bug-list">
        <BugItem
          v-for="bug in paginatedBugs"
          :key="bug.id"
          :id="bug.id"
          :status="bug.status"
          :summary="bug.summary"
          :version="bug.version"
          :product="bug.product"
          :component="bug.component"
          :cardWidth="'100%'"
          @bug-info="handleViewBugInfo"
        />
      </div>
      <el-pagination
        background
        layout="prev, pager, next"
        :total="totalBugs"
        :page-size="20"
        @current-change="handlePageChange"
      />
    </el-main>
  </el-container>
</template>

<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import axios from "axios";
import BugItem from "../components/BugItem.vue";

const baseURL = process.env.VUE_APP_BASE_URL;

const route = useRoute();
const router = useRouter();

// 左侧标签列表
const productComponentTypes = ref([{ product: "", components: [] }]);
const statusTypes = ref([]);
const platformTypes = ref([]);
const companyTypes = ref([]);
// 右侧bug列表
const currentTitle = ref("");
const currentBugs = ref([]);
const currentPage = ref(1);
const totalBugs = ref(0);
const activeMenuItem = ref("");

// 分页相关
const paginatedBugs = computed(() => {
  const start = (currentPage.value - 1) * 10;
  const end = start + 10;
  return currentBugs.value.slice(start, end);
});

const handlePageChange = (page) => {
  currentPage.value = page;
};

// 更新展示类型
const updateExhibitionType = async () => {
  activeMenuItem.value = route.params.type;
  currentTitle.value = route.params.type;
  await fetchProductComponentTypes();
  await fetchStatusTypes();
  await fetchPlatformTypes();
  await fetchCompanyTypes();
  updateInitBugs(activeMenuItem.value);
};

// 获取初始bugs
const updateInitBugs = async (type) => {
  switch(type){
    case "overview":
      await fetchAllBugs();
      break;
    case "product-components":
      await fetchProductComponentBugs(productComponentTypes.value[0].product, productComponentTypes.value[0].components[0]);
      break;
    case "status":
      await fetchStatusBugs(statusTypes.value[0]);
      break;
    case "platform":
      await fetchPlatformBugs(platformTypes.value[0]);
      break;
    case "company":
      await fetchCompanyBugs(companyTypes.value[0]);
      break;
    default:
      await fetchAllBugs();
  }
}

// 获取类型的函数
const fetchProductComponentTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/product-components/`);
    const data = response.data;

    // 将数据转换为需要的格式
    const groupedData = data.reduce((acc, { product, component }) => {
      const existingProduct = acc.find((p) => p.product === product);
      if (existingProduct) {
        existingProduct.components.push(component);
      } else {
        acc.push({ product, components: [component] });
      }
      return acc;
    }, []);

    productComponentTypes.value = groupedData;
  } catch (error) {
    ElMessage.error("获取产品组件类型错误：" + error.message);
  }
};

const fetchStatusTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/statuses/`);
    statusTypes.value = response.data;
  } catch (error) {
    ElMessage.error("获取状态类型错误：" + error.message);
  }
};

const fetchPlatformTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/platforms/`);
    platformTypes.value = response.data;
  } catch (error) {
    ElMessage.error("获取平台类型错误：" + error.message);
  }
};

const fetchCompanyTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/companies/`);
    companyTypes.value = response.data.data.map((company) => company.name);
  } catch (error) {
    ElMessage.error("获取公司类型错误：" + error.message);
  }
};

// 获取bugs的列表的函数
const fetchProductComponentBugs = async (product, component) => {
  try {
    const response = await axios.get(
      `${baseURL}/bugs/product-component-bugs?product=${product}&component=${component}`
    );
    currentBugs.value = response.data;
    totalBugs.value = response.data.length;
  } catch (error) {
    ElMessage.error("获取产品组件的bugs错误：" + error.message);
  }
};

const fetchStatusBugs = async (status) => {
  try {
    const response = await axios.get(
      `${baseURL}/bugs/status-bugs-list?status=${status}`
    );
    currentBugs.value = response.data;
    totalBugs.value = response.data.length;
  } catch (error) {
    ElMessage.error("获取状态的bugs错误：" + error.message);
  }
};

const fetchPlatformBugs = async (platform) => {
  try {
    const response = await axios.get(
      `${baseURL}/bugs/platform-bugs?platform=${platform}`
    );
    currentBugs.value = response.data;
    totalBugs.value = response.data.length;
  } catch (error) {
    ElMessage.error("获取平台的bugs错误：" + error.message);
  }
};

const fetchCompanyBugs = async (company) => {
  try {
    const response = await axios.get(
      `${baseURL}/bugs/company-bugs?company=${company}`
    );
    currentBugs.value = response.data;
    totalBugs.value = response.data.length;
  } catch (error) {
    ElMessage.error("获取公司的bugs错误：" + error.message);
  }
};

const fetchAllBugs = async (string) => {
  currentTitle.value = string;
  try {
    const response = await axios.get(
      `${baseURL}/bugs/all-bugs`
    );
    currentBugs.value = response.data;
    totalBugs.value = response.data.length;
  } catch (error) {
    ElMessage.error("获取公司的bugs错误：" + error.message);
  }
};

// 处理菜单选择
const handleMenuSelect = (index) => {
  activeMenuItem.value = index;
};
const selectStatus = (subType, index) => {
  fetchStatusBugs(subType);
  currentTitle.value = index;
};
const selectPlatform = (subType, index) => {
  fetchPlatformBugs(subType);
  currentTitle.value = index;
};
const selectCompany = (subType, index) => {
  fetchCompanyBugs(subType);
  currentTitle.value = index;
};
const selectProductComponent = (product, component, index) => {
  fetchProductComponentBugs(product, component);
  currentTitle.value = index;
};

onMounted(() => {
  updateExhibitionType();
});

watch(
  () => route.params,
  () => {
    updateExhibitionType();
  }
);

// 处理bug详情跳转
const handleViewBugInfo = (id) => {
  router.push({ name: "bug-info", params: { id } });
};
</script>

<style scoped>
.custom-aside {
  background-color: #d2def0;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.el-menu {
  border-right: none;
  overflow-y: auto;
}

.menu-item {
  background-color: #f5f2f2;
  margin-bottom: 5px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.menu-item:hover {
  background-color: #e6f7ff;
}

.custom-main {
  background-color: #fefff6;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.bug-list {
  display: flex;
  flex-wrap: wrap;
}

.bug-list > * {
  margin: 10px;
  width: calc(50% - 20px); /* 每行两个 */
}

.el-pagination {
  margin-top: 20px;
  text-align: center;
}

.container-bg {
  background-color: rgb(219, 227, 218);
  height: 95vh;
  overflow-y: auto;
}
</style>