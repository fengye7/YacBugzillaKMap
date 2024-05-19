<template>
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
      <el-menu-item index="/home">首页</el-menu-item>
      <el-menu-item index="/exhibition">数据展览</el-menu-item>
      <el-menu-item index="/knowledgeMap">数据图谱</el-menu-item>
      <el-menu-item index="/analysis">数据分析</el-menu-item>
      <el-menu-item index="/statistics">数据统计</el-menu-item>
      <el-menu-item index="/prediction">预测分析</el-menu-item>
    </el-menu>
  </el-header>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const activeMenu = ref("/home");
const router = useRouter();

const handleMenuSelect = (index) => {
  router.push(index);
  activeMenu.value = index;
};
</script>

<style scoped>
.logo {
  font-size: 28px;
  color: #0a5991;
  margin-right: 20px;
}
</style>
