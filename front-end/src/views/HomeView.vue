<template>
  <div class="home">
    <!-- 导航栏 -->
    <el-header>
      <div class="logo">Yocto项目分析平台</div>
      <el-menu
        class="el-menu-demo"
        v-model="activeMenu"
        :default-active="activeMenu"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        mode="horizontal"
        @select="handleMenuSelect"
      >
        <el-menu-item index="home">首页</el-menu-item>
        <el-menu-item index="analysis">数据分析</el-menu-item>
        <el-menu-item index="prediction">预测分析</el-menu-item>
        <el-menu-item index="knowledgeMap">数据图谱</el-menu-item>
      </el-menu>
    </el-header>

    <!-- 页面内容 -->
    <el-main>
      <div v-if="activeMenu === 'home'" class="page-content">
        <h1>欢迎来到Yocto项目分析平台</h1>
        <p>
          通过对论坛网站数据的整理和用户画像分析，我们帮助您深入了解Yocto项目在市场中的竞争情况，预测项目的发展方向，并提供决策支持。
        </p>
        <p>请选择上方菜单开始数据分析和预测分析。</p>
      </div>

      <!-- 其他页面内容 -->
      <!-- <div v-else-if="activeMenu === 'analysis'"> 数据分析内容 </div>
      <div v-else-if="activeMenu === 'prediction'"> 预测分析内容 </div> -->
      <div v-else-if="activeMenu === 'knowledgeMap'"> 
        <h1>数据图谱</h1>
        <k-map-charts/>
      </div>
    </el-main>

    <!-- 页脚 -->
    <el-footer class="footer">
      <div class="footer-content">
        <p>版权所有 &copy; 2024 Yocto项目分析平台</p>
      </div>
    </el-footer>
  </div>
</template>

<script setup>
import { ref } from "vue";
import KMapCharts from '../components/KMapCharts.vue'

const activeMenu = ref("home");

const handleMenuSelect = (index) => {
  activeMenu.value = index;
};
</script>

<style scoped>
.home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.logo {
  font-size: 28px;
  color: #0a5991;
  margin-right: 20px;
}

.page-content {
  padding: 20px;
}

.footer {
  background-color: #303133;
  color: #fff;
  text-align: center;
  padding: 20px;
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
