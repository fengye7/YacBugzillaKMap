<template>
  <el-card shadow="hover">
    <template #header>
      <h1 class="header-title">数据分析图谱 - Yocto Bugzilla 平台</h1>
    </template>

    <el-container class="content-container">
      <el-main class="main-content">
        <div class="description">
          <h2 class="section-title">数据图谱</h2>
          <p>右侧输入后，您可以在下方图表中查看 Yocto Bugzilla 平台的一个基于(“产品”->“组件”)(“账户”->"产品组件")的相关数据分析，用于显示目标公司的成员关注哪些产品组件。</p>
        </div>

        <div class="chart-section">
          <k-map-charts/>
        </div>
      </el-main>
    </el-container>
  </el-card>
</template>

<script setup>
import KMapCharts from '../components/KMapCharts.vue'
import { ElCard, ElContainer, ElMain } from 'element-plus'
import 'element-plus/dist/index.css'
</script>

<style scoped>
.el-card {
  background-color: #f9f9f9;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
}

.el-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.header-title {
  color: #333;
  font-size: 24px;
  text-align: center;
  font-weight: bold;
  margin: 0;
}

.content-container {
  margin-top: 20px;
}

.main-content {
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.5s ease-in-out;
}

.section-title {
  color: #4caf50;
  font-size: 20px;
  border-bottom: 2px solid #4caf50;
  padding-bottom: 5px;
}

.description {
  margin-bottom: 20px;
}

.chart-section {
  margin-top: 20px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
