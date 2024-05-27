<template>
  <el-card class="comment-list">
    <h3>Comments</h3>
    <el-list>
      <el-list-item v-for="comment in comments" :key="comment.id" class="comment-item">
        <el-card class="comment-card">
          <p class="comment-header">
            <strong>{{ comment.commentator }}</strong> at {{ comment.time }}
          </p>
          <p class="comment-content">{{ comment.content }}</p>
        </el-card>
      </el-list-item>
    </el-list>
  </el-card>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  comments: {
    type: Array,
    required: true
  }
});
console.log(props.comments);
</script>

<style scoped>
.comment-list {
  margin-top: 20px;
  background-color: rgb(251, 251, 236);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.comment-item {
  margin-bottom: 10px;
}

.comment-card {
  background: linear-gradient(135deg, #f9f9f9, #f1f1f1);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
  padding: 10px;
}

.comment-card:hover {
  transform: translateY(-5px);
}

.comment-header {
  background: #eef2f7;
  padding: 8px;
  border-radius: 4px 4px 0 0;
  border-bottom: 1px solid #dce1e7;
  color: rgb(80, 26, 87);
  font-size: 18px;
}

.comment-content {
  padding: 8px;
  background: #fff;
  border-radius: 0 0 4px 4px;
  font-family: serif;
  font-size: 14px;
}
</style>
