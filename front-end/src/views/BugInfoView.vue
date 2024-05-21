<!-- BugInfoView.vue -->
<template>
  <el-container class="bug-info-view">
    <el-header>
      <h2>Bug Details</h2>
    </el-header>
    <el-main>
      <div v-if="bug">
        <el-card>
          <h3>{{ bug.product }} - {{ bug.component }}</h3>
          <el-tag type="info">Bug-{{ bug.id }}</el-tag>
          <el-tag>{{ bug.status }}</el-tag>
          <p><strong>Summary:</strong> {{ bug.summary }}</p>
          <p><strong>Version:</strong> {{ bug.version }}</p>
          <p><strong>Priority:</strong> {{ bug.priority }}</p>
          <p><strong>Severity:</strong> {{ bug.severity }}</p>
          <p><strong>Platform:</strong> {{ bug.platform }}</p>
          <p><strong>Operating System:</strong> {{ bug.op_sys }}</p>
          <p><strong>Assignee:</strong> {{ bug.assignee }}</p>
          <p><strong>QA:</strong> {{ bug.QA }}</p>
          <p><strong>CC List:</strong> {{ bug.ccList }}</p>
          <p>
            <strong>Reported By:</strong> {{ reported.user }} at
            {{ reported.time }}
          </p>
          <p>
            <strong>Last Modified By:</strong> {{ modified.user }} at
            {{ modified.time }}
          </p>
        </el-card>
        <el-card>
          <bug-comments :comments="comments"></bug-comments>
        </el-card>
      </div>
      <div v-else>
        <el-card>
          <p>Loading...</p>
        </el-card>
      </div>
    </el-main>
  </el-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import BugComments from "../components/BugComments.vue";

const route = useRoute();
const bug = ref(null);
const reported = ref({});
const modified = ref({});
const comments = ref([]);

onMounted(() => {
  const bugId = route.params.id;
  fetchBugDetails(bugId);
  fetchReportedDetails(bugId);
  fetchModifiedDetails(bugId);
  fetchComments(bugId);
});

const fetchBugDetails = (id) => {
  // 模拟API调用，实际使用时应替换为真实的API请求
  const fakeData = [
    {
      id: 1,
      status: "Open",
      summary: "Bug 1 summary",
      version: "1.0",
      product: "Product A",
      component: "Component X",
      priority: "High",
      severity: "Critical",
      platform: "Platform A",
      op_sys: "Linux",
      assignee: "Assignee A",
      QA: "QA A",
      ccList: "user1@example.com, user2@example.com",
    },
    // 添加更多的bug数据
  ];

  bug.value = fakeData.find((b) => b.id === parseInt(id));
};

const fetchReportedDetails = () => {
  // 模拟API调用，实际使用时应替换为真实的API请求
  reported.value = {
    user: "Reporter A",
    time: "2024-01-01 12:00:00",
  };
};

const fetchModifiedDetails = () => {
  // 模拟API调用，实际使用时应替换为真实的API请求
  modified.value = {
    user: "Modifier B",
    time: "2024-01-02 15:00:00",
  };
};

const fetchComments = () => {
  // 模拟API调用，实际使用时应替换为真实的API请求
  comments.value = [
    {
      id: 1,
      commentator: "User 1",
      content: "This is a comment.",
      time: "2024-01-01 13:00:00",
    },
    {
      id: 2,
      commentator: "User 2",
      content: "This is another comment.",
      time: "2024-01-02 14:00:00",
    },
    // 添加更多的评论数据
  ];
};
</script>

<style scoped>
.bug-info-view {
  padding: 20px;
}

.el-header h2 {
  margin: 0;
  font-size: 24px;
}
</style>
