<template>
  <el-container>
    <el-aside width="400px">
      <el-menu :default-active="activeMenuItem" @select="handleMenuSelect">
        <el-menu-item index="overview">总览</el-menu-item>
        <el-submenu index="product-components">
          <template #title>产品组件</template>
          <el-menu-item
            v-for="product in productComponentTypes"
            :key="product.product"
            :index="product.product"
            @click="selectSubCategory(product.product)"
          >
            {{ product.product }}
            <el-menu
              v-if="subCategory.value === product.product"
              @select="selectComponent"
            >
              <el-menu-item
                v-for="component in product.components"
                :key="component"
                :index="component"
              >
                {{ component }}
              </el-menu-item>
            </el-menu>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="status">
          <template #title>Status</template>
          <el-menu-item
            v-for="status in statusTypes"
            :key="status"
            :index="status"
          >
            {{ status }}
          </el-menu-item>
        </el-submenu>
        <el-submenu index="platform">
          <template #title>Platform</template>
          <el-menu-item
            v-for="platform in platformTypes"
            :key="platform"
            :index="platform"
          >
            {{ platform }}
          </el-menu-item>
        </el-submenu>
        <el-submenu index="company">
          <template #title>公司</template>
          <el-menu-item
            v-for="company in companyTypes"
            :key="company"
            :index="company"
          >
            {{ company }}
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-main>
      <h3>{{ currentTitle }}</h3>
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
  const start = (currentPage.value - 1) * 20;
  const end = start + 20;
  return currentBugs.value.slice(start, end);
});

const handlePageChange = (page) => {
  currentPage.value = page;
};

// 更新展示类型
const updateExhibitionType = async () => {
  const type = route.params.type;
  const subType = route.params.subType || "";
  const component = route.params.component || "";

  activeMenuItem.value = type;

  currentTitle.value = `${type} - ${subType} - ${component}`;

  switch (type) {
    case "product-components":
      await fetchProductComponentTypes();
      if (subType) {
        const selectedProduct = productComponentTypes.value.find(
          (p) => p.product === subType
        );
        if (selectedProduct && selectedProduct.components.length) {
          await fetchProductComponentBugs(
            subType,
            component || selectedProduct.components[0]
          );
        }
      }
      break;
    case "status":
      await fetchStatusTypes();
      if (subType) {
        await fetchStatusBugs(subType);
      }
      break;
    case "platform":
      await fetchPlatformTypes();
      if (subType) {
        await fetchPlatformBugs(subType);
      }
      break;
    case "company":
      await fetchCompanyTypes();
      if (subType) {
        await fetchCompanyBugs(subType);
      }
      break;
    default:
      break;
  }
};

// 获取类型的函数
const fetchProductComponentTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/product-components/`);
    productComponentTypes.value = response.data;
  } catch (error) {
    ElMessage.error("获取产品组件类型错误：" + error.message);
  }
};

const fetchStatusTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/status-types/`);
    statusTypes.value = response.data;
  } catch (error) {
    ElMessage.error("获取状态类型错误：" + error.message);
  }
};

const fetchPlatformTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/platform-types/`);
    platformTypes.value = response.data;
  } catch (error) {
    ElMessage.error("获取平台类型错误：" + error.message);
  }
};

const fetchCompanyTypes = async () => {
  try {
    const response = await axios.get(`${baseURL}/bugs/company-types/`);
    companyTypes.value = response.data;
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
      `${baseURL}/bugs/status-bugs?status=${status}`
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

const handleMenuSelect = (index) => {
  router.push({ name: "DataExhibition", params: { type: index } });
};

const selectSubCategory = (subType) => {
  router.push({
    name: "DataExhibition",
    params: { type: activeMenuItem.value, subType },
  });
};

const selectComponent = (component) => {
  router.push({
    name: "DataExhibition",
    params: {
      type: activeMenuItem.value,
      subType: subCategory.value,
      component,
    },
  });
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
</script>


<style scoped>
.el-container {
  display: flex;
  height: 100vh;
}

.el-aside {
  width: 400px;
  background-color: #f5f5f5;
  padding: 20px;
  overflow-y: auto;
}

.el-menu {
  width: 100%;
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
</style>