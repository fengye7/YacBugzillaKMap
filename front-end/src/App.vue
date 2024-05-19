<template>
  <div id="app">
    <!-- 导航栏 -->
    <NavBar />

    <!-- 页面内容 -->
    <router-view />

    <!-- 页脚 -->
    <FooterBar />
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
import FooterBar from "./components/FooterBar.vue";
</script>

<style>
/* 全局样式 */
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

router-view {
  flex: 1;
  padding-bottom: 60px; /* 给路由视图内容预留空间，以免被固定的页脚遮挡 */
}
</style>
