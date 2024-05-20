<template>
  <el-header class="navbar">
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
      <el-menu-item index="exhibition">数据展览</el-menu-item>
      <el-menu-item index="knowledgeMap">数据图谱</el-menu-item>
      <el-menu-item index="analysis">数据分析</el-menu-item>
      <el-menu-item index="statistics">数据统计</el-menu-item>
      <el-menu-item index="prediction">预测分析</el-menu-item>
    </el-menu>
  </el-header>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const activeMenu = ref("home");
const router = useRouter();

const handleMenuSelect = (index) => {
  activeMenu.value = index;
  router.push({ name: index }); // 路由跳转
};
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  background-color: #545c64;
  display: flex;
  align-items: center;
  height: 60px;
}

.logo {
  font-size: 28px;
  color: #ffd04b;
  margin-right: 20px;
  padding-left: 20px;
  line-height: 60px; /* 垂直居中 */
  background-color: #545c64; /* 与导航栏一致 */
  white-space: nowrap; /* 防止文字换行 */
}

.el-menu-demo {
  flex: 1; /* 占据剩余空间 */
  background-color: #545c64;
  display: flex;
  justify-content: flex-end; /* 菜单项靠右对齐 */
}

.el-menu-item {
  line-height: 60px;
  white-space: nowrap; /* 防止文字换行 */
}
</style>
