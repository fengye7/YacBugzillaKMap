<template>
  <div id="app">
    <!-- 导航栏 -->
    <NavBar class="navbar" />

    <!-- 页面内容 -->
    <div class="content">
      <router-view />
    </div>

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
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000; /* 确保导航栏在最上层 */
}

.content {
  flex: 1;
  overflow-y: auto; /* 如果内容过长，启用垂直滚动条 */
  padding-top: 60px; /* 导航栏的高度是60px */
}

</style>
