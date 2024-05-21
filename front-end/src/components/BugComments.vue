<!-- BugComments.vue -->
<template>
  <div class="comment-list">
    <h3>Comments</h3>
    <el-list>
      <el-list-item v-for="comment in comments" :key="comment.id" class="comment-item">
        <el-card>
          <p><strong>{{ comment.commentator }}</strong> at {{ comment.time }}</p>
          <p>{{ comment.content }}</p>
        </el-card>
      </el-list-item>
    </el-list>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  comments: {
    type: Array,
    required: true
  }
});
console.log(props);
</script>

<style scoped>
.comment-list {
  margin-top: 20px;
}

.comment-item {
  margin-bottom: 10px;
}
</style>
