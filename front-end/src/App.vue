<template>
  <div id="app">
    <!-- 导航栏 -->
    <NavBar />

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
  /* overflow: hidden; */
}

.content {
  flex: 1;
  overflow-y: auto; /* 如果内容过长，启用垂直滚动条 */
}

</style>
