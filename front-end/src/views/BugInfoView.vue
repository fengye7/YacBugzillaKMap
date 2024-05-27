<template>
  <el-container class="bug-info-view">
    <el-header>
      <h2>Bug Details</h2>
    </el-header>
    <el-main>
      <div v-if="bug">
        <el-card class="bug-card">
          <h3>{{ bug.product }} - {{ bug.component }}</h3>
          <el-tag type="info">Bug-{{ bug.id }}</el-tag>
          <el-tag>{{ bug.status }}</el-tag>
          <p class="info-item"><strong>Summary:</strong> <span>{{ bug.summary }}</span></p>
          <p class="info-item"><strong>Version:</strong> <span>{{ bug.version }}</span></p>
          <p class="info-item"><strong>Priority:</strong> <span>{{ bug.priority }}</span></p>
          <p class="info-item"><strong>Severity:</strong> <span>{{ bug.severity }}</span></p>
          <p class="info-item"><strong>Platform:</strong> <span>{{ bug.platform }}</span></p>
          <p class="info-item"><strong>Operating System:</strong> <span>{{ bug.op_sys }}</span></p>
          <p class="info-item"><strong>Assignee:</strong> <span>{{ bug.assignee }}</span></p>
          <p class="info-item"><strong>QA:</strong> <span>{{ bug.QA }}</span></p>
          <p class="info-item"><strong>CC List:</strong> <span>{{ bug.ccList }}</span></p>
          <p class="info-item"><strong>Reported By:</strong> <span>{{ reported.user }} at {{ reported.time }}</span></p>
          <p class="info-item">
            <strong>Modified By:</strong>
            <ol>
              <li v-for="mod in modifieds" :key="mod.id">
                {{ mod.user }} at {{ mod.time }}
              </li>
            </ol>
          </p>
        </el-card>
        <!--评论区域-->
          <bug-comments v-if="comments.length > 0" :comments="comments"></bug-comments>
      </div>
      <div v-else>
        <el-card class="loading-card">
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
const modifieds = ref([]);
const comments = ref([]);

onMounted(() => {
  const bugId = route.params.id;
  fetchBugDetails(bugId);
});

const fetchBugDetails = async (id) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/bugs/bug-info/${id}/`, {
      method: "GET",
      headers: {
        accept: "application/json",
        "X-CSRFToken":
          "SefV0fahdjtPu3u5ycuda9wAVMd7L9TJ3PygsawVMfdvQig5KndvjJmQjShhPFre",
      },
    });
    const data = await response.json();
    bug.value = data.bug;
    reported.value = data.reported;
    modifieds.value = data.modifieds;
    comments.value = data.comments;
  } catch (error) {
    console.error("Error fetching bug details:", error);
  }
};
</script>

<style scoped>
.bug-info-view {
  padding: 20px;
  background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: #95abc4;
}

.el-header {
  background: #4a90e2;
  color: #fff;
  padding: 10px;
  border-radius: 8px 8px 0 0;
}

.el-header h2 {
  margin: 0;
  font-size: 24px;
  animation: fadeIn 1s ease-in-out;
}

.bug-card,
.loading-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
  margin-bottom: 20px;
}

.bug-card:hover,
.comments-card:hover {
  transform: translateY(-5px);
}

.bug-card h3 {
  color: #333;
  font-size: 20px;
}

.el-tag {
  margin-right: 5px;
}

.info-item {
  background: #f9fafb;
  border: 1px solid #e1e4e8;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
}

ol {
  padding-left: 20px;
}

ol li {
  background: #f9fafb;
  border: 1px solid #e1e4e8;
  padding: 5px;
  border-radius: 4px;
  margin-bottom: 5px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

strong {
  color: #8aaace;
}
</style>
