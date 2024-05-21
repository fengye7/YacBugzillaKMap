<!-- BugCard.vue -->
<template>
  <el-card :style="{ width: cardWidth }" class="bug-card">
    <div class="bug-card-content">
      <div class="header">
        <h4>{{ product }} - {{ component }}</h4>
        <el-tag type="info">Bug-{{id}}</el-tag>
        <el-tag>{{ status }}</el-tag>
      </div>
      <div class="summary">{{ summary }}</div>
      <div class="footer">
        <span>Version: {{ version }}</span>
        <el-button type="text" @click="viewBugDetails">View Details</el-button>
      </div>
    </div>
  </el-card>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

// 定义props
const props = defineProps({
  id: Number,
  status: String,
  summary: String,
  version: String,
  product: String,
  component: String,
  cardWidth: {
    type: String,
    default: '300px' // 默认宽度
  }
});

// 定义emits
const emit = defineEmits(['bug-info']);

// 查看bug详情
const viewBugDetails = () => {
  emit('bug-info', props.id);
};
</script>

<style scoped>
.bug-card {
  margin-bottom: 20px;
  background-color: azure;
}

.bug-card-content {
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.summary {
  flex: 1;
  margin-bottom: 10px;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
