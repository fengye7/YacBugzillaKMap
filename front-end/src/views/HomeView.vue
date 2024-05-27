<template>
  <el-container class="home">
    <!-- 中部占位图片（文字在图片上面） -->
    <div class="image-wrapper">
      <img
        src="@/assets/imgs/YactoBg.jpg"
        alt="Yacto Background"
        class="background-image"
      />
      <div class="overlay">
        <h1>欢迎来到Yocto项目分析平台</h1>
        <p>
          通过对论坛网站数据的整理和用户画像分析，我们帮助您深入了解Yocto项目在市场中的竞争情况，预测项目的发展方向，并提供决策支持。
        </p>
        <p>请选择上方菜单开始数据分析和预测分析。</p>
      </div>
    </div>

    <!-- 下方资源分类列表和最新bug区域 -->
    <el-main class="resource-wrapper">
      <!-- 资源分类列表区域 -->
      <div class="resource-section">
        <h2>资源分类</h2>
        <div class="resource-list">
          <el-card class="resource-item" @click="navigateTo('overview')">
            <el-icon><List /></el-icon>
            <!-- <el-row/>换行 -->
            <el-row/>
            <span>总览</span>
          </el-card>
          <el-card
            class="resource-item"
            @click="navigateTo('product-components')"
          >
            <el-icon><Grid /></el-icon>
            <el-row/>
            <span>产品组件</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('status')">
            <el-icon><ElementPlus /></el-icon>
            <el-row/>
            <span>状态</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('platform')">
            <el-icon><Cpu /></el-icon>
            <el-row/>
            <span>平台</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('company')">
            <el-icon><House /></el-icon>
            <el-row/>
            <span>公司</span>
          </el-card>
        </div>
      </div>

      <!-- 最新bug列表区域 -->
      <div class="bug-section">
        <h2>Latest bugs</h2>
        <div class="bug-list">
          <BugItem
            v-for="bug in bugs"
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
      </div>
    </el-main>
  </el-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { List, Grid, ElementPlus, Cpu, House } from "@element-plus/icons-vue";
import BugItem from '../components/BugItem.vue';

const bugs = ref([]);
const router = useRouter();

onMounted(() => {
  fetchLatestBugs();
});

const fetchLatestBugs = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/bugs/latest-bugs/', {
      method: 'GET',
      headers: {
        'accept': 'application/json',
        'X-CSRFToken': 'SefV0fahdjtPu3u5ycuda9wAVMd7L9TJ3PygsawVMfdvQig5KndvjJmQjShhPFre'
      }
    });
    const data = await response.json();
    bugs.value = data;
  } catch (error) {
    console.error("Error fetching latest bugs:", error);
  }
};

const navigateTo = (type) => {
  router.push({ name: "exhibition", params: { type } });
};

const handleViewBugInfo = (id) => {
  router.push({ name: 'bug-info', params: { id } });
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f2f5;
}

.image-wrapper {
  position: relative;
  width: 100%;
  max-width: 100vw;
  height: 400px;
  margin-bottom: 20px;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  text-align: center;
  border-radius: 10px;
}

.resource-wrapper {
  display: flex;
  width: 100%;
  max-width: 100vw;
  justify-content: space-between;
  margin-top: 20px;
}

.resource-section {
  flex: 7;
  margin-right: 20px;
  position: relative;
  background-image: url('@/assets/imgs/textureBg.jpeg');
  background-size: cover;
  background-position: center;
  border-radius: 5px;
  overflow: hidden;
}

.resource-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 1;
}

.resource-section > * {
  position: relative;
  z-index: 2;
}

.bug-section {
  flex: 3;
  max-height: 600px;
  overflow-y: auto;
}

.resource-section,
.bug-section {
  background-color: rgba(255, 255, 255, 0.5);
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.resource-section h2,
.bug-section h2 {
  margin-bottom: 10px;
}

.resource-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.resource-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 30px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  flex: 1;
  text-align: center;
}

.el-icon {
  font-size: 45px;
}

.bug-list ul {
  list-style: none;
  padding: 0;
}

.bug-item {
  margin-bottom: 10px;
}

.bug-item .el-card {
  cursor: pointer;
}
</style>
