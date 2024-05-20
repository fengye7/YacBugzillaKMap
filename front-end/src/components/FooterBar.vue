<template>
  <el-footer class="footer">
    <div class="footer-content">
      <p>版权所有 &copy; 2024 Yacto项目分析平台</p>
      <p>
        <a href="https://www.yactoproject.com" target="_blank" rel="noopener noreferrer">
          Yacto平台链接
        </a>
        <el-icon><CloseBold /></el-icon>
        <a href="https://bugzilla.yoctoproject.org/" target="_blank" rel="noopener noreferrer">
          Yacto Bugzilla链接
        </a>
      </p>
        <a href="https://github.com/fengye7/YacBugzillaKMap" target="_blank" rel="noopener noreferrer">
          本项目分析平台链接
        </a>
      <p>
      </p>
      <p>
        <el-icon><ChatDotRound /></el-icon>
        <a href="tencent://Message/?Uin=2518529668" target="_blank" rel="noopener noreferrer">
          QQ: 2518529668
        </a>
      </p>
      <p>项目组信息: Yacto项目组</p>
    </div>
  </el-footer>
</template>

<script setup>
import { ChatDotRound, CloseBold } from '@element-plus/icons-vue'
</script>

<style scoped>
.footer {
  position: relative;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-color: #303133;
  color: #fff;
  text-align: center;
  padding: 20px;
  z-index: 1000;
}

.footer-content p {
  margin: 5px 0;
}

.footer-content a {
  color: #ffd04b;
  text-decoration: none;
}

.footer-content a:hover {
  text-decoration: underline;
}

.el-icon {
  vertical-align: middle;
  margin-right: 5px;
}
</style>
