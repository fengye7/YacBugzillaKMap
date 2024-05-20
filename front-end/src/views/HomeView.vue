<template>
  <el-container class="home">
    <!-- 中部占位图片（文字在图片上面） -->
    <div class="image-wrapper">
      <img src="@/assets/imgs/YactoBg.jpg" alt="Yacto Background" class="background-image" />
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
            <span>总览</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('product-components')">
            <el-icon><Grid /></el-icon>
            <span>产品组件</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('status')">
            <el-icon><ElementPlus /></el-icon>
            <span>状态</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('platform')">
            <el-icon><Cpu /></el-icon>
            <span>平台</span>
          </el-card>
          <el-card class="resource-item" @click="navigateTo('company')">
            <el-icon><House /></el-icon>
            <span>公司</span>
          </el-card>
        </div>
      </div>

      <!-- 最新bug列表区域 -->
      <div class="bug-section">
        <h2>最新10个bug</h2>
        <el-list>
          <el-list-item v-for="bug in bugs" :key="bug.id" class="bug-item">
            <el-card @click="navigateToBug(bug.id)">
              {{ bug.title }}
            </el-card>
          </el-list-item>
        </el-list>
      </div>
    </el-main>
  </el-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { List, Grid, ElementPlus, Cpu, House } from '@element-plus/icons-vue';

// 模拟bug数据
const bugs = ref([]);
const router = useRouter();

onMounted(() => {
  // 这里你可以使用实际的API调用来获取最新的10个bug
  bugs.value = [
    { id: 1, title: 'Bug 1' },
    { id: 2, title: 'Bug 2' },
    { id: 3, title: 'Bug 3' },
    { id: 4, title: 'Bug 4' },
    { id: 5, title: 'Bug 5' },
    { id: 6, title: 'Bug 6' },
    { id: 7, title: 'Bug 7' },
    { id: 8, title: 'Bug 8' },
    { id: 9, title: 'Bug 9' },
    { id: 10, title: 'Bug 10' },
  ];
});

// 导航到资源页面
const navigateTo = (route) => {
  router.push({ name: route });
};

// 导航到具体的bug页面
const navigateToBug = (id) => {
  router.push({ name: 'bug-detail', params: { id } });
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
}

.bug-section {
  flex: 3;
}

.resource-section, .bug-section {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.resource-section h2, .bug-section h2 {
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
