<template>
  <div>
    <div v-if="exhibition_type === 'overview'">
      <!-- 总览内容 -->
      <h3>总览</h3>
      <p>这里是总览内容...</p>
    </div>
    <div v-else-if="exhibition_type === 'product-components'">
      <!-- 产品组件内容 -->
      <h3>产品组件</h3>
      <p>这里是产品组件内容...</p>
    </div>
    <div v-else-if="exhibition_type === 'status'">
      <!-- 状态内容 -->
      <h3>状态</h3>
      <p>这里是状态内容...</p>
    </div>
    <div v-else-if="exhibition_type === 'platform'">
      <!-- 平台内容 -->
      <h3>平台</h3>
      <p>这里是平台内容...</p>
    </div>
    <div v-else-if="exhibition_type === 'company'">
      <!-- 公司内容 -->
      <h3>公司</h3>
      <p>这里是公司内容...</p>
    </div>
    <div v-else>
      <!-- 默认内容 -->
      <h3>默认内容</h3>
      <p>这里是默认内容...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const exhibition_type = ref("");

const updateExhibitionType = () => {
  exhibition_type.value = route.params.type;
};

onMounted(() => {
  updateExhibitionType();
});

watch(
  () => route.params.type,
  (newType) => {
    exhibition_type.value = newType;
  }
);
</script>

<style scoped>
/* 添加你的样式 */
</style>
