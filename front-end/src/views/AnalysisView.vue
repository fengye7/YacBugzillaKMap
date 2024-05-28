<template>
  <el-card shadow="hover">
    <template #header>
      <h1 class="header-title">数据分析 - Yocto Bugzilla 平台</h1>
    </template>

    <div class="analysis-section">
      <h2 class="section-title">1. 网站功能</h2>
      <p>网站可以执行以下操作：</p>
      <ul>
        <li class="feature">提交 Bug（Enter bug）：选择分类、产品、组件进行 Bug 提交。</li>
        <li class="feature">搜索 Bug（Search）：按产品类别和组件搜索 Bug。</li>
        <li class="feature">浏览 Bug（Browse）：按类别浏览 Bug。</li>
        <li class="feature">报告（Report）：提供相关的图表分析。</li>
        <li class="feature">创建账户和使用 Bugzilla 指南。</li>
      </ul>
    </div>

    <div class="analysis-section">
      <h2 class="section-title">2. 可获取的数据</h2>
      <p>可以获取以下数据，用于辅助分析用户活跃程度和开发者：</p>
      <ul>
        <li><strong>Summary</strong>：问题的一句话摘要。</li>
        <li><strong>Status</strong>：Bug 的当前状态及分辨率。</li>
        <li><strong>Alias</strong>：Bug 的唯一短文本名称。</li>
        <li><strong>Product and Component</strong>：Bug 按 Product 和 Component 划分。</li>
        <li><strong>Version</strong>：受 Bug 报告影响的版本。</li>
        <li><strong>Hardware (Platform and OS)</strong>：发现 Bug 的计算环境。</li>
        <li><strong>Importance (Priority and Severity)</strong>：Bug 的优先级和严重性。</li>
        <li><strong>Target Milestone</strong>：未来修复 Bug 的版本。</li>
        <li><strong>Assigned To</strong>：负责修复 Bug 的人员。</li>
        <li><strong>QA Contact</strong>：负责质量保证的人员。</li>
        <li><strong>URL</strong>：与 Bug 关联的 URL。</li>
        <li><strong>Whiteboard</strong>：用于添加短注释和标签的自由格式文本区域。</li>
        <li><strong>Keywords</strong>：用于标记和分类 Bug 的关键字。</li>
        <li><strong>Personal Tags</strong>：个人标签，仅作者可见和编辑。</li>
        <li><strong>Dependencies (Depends On and Blocks)</strong>：Bug 的依赖关系。</li>
        <li><strong>Reported</strong>：提交 Bug 的人及时间。</li>
        <li><strong>Modified</strong>：上次更改 Bug 的日期和时间。</li>
        <li><strong>CC List</strong>：在 Bug 更改时收到邮件的人员列表。</li>
        <li><strong>Ignore Bug Mail</strong>：忽略 Bug 邮件设置。</li>
        <li><strong>See Also</strong>：相关的 Bug。</li>
        <li><strong>Flags</strong>：设置在 Bug 或附件上的状态标志。</li>
        <li><strong>Time Tracking</strong>：用于时间跟踪的表单。</li>
        <li><strong>Attachments</strong>：附加到 Bug 的文件。</li>
        <li><strong>Additional Comments</strong>：补充说明。</li>
      </ul>
    </div>

    <div class="analysis-section">
      <h2 class="section-title">3. 活跃度分析</h2>
      <p>通过查看近1/7天的 Bug 信息，我们可以分析项目的活跃度。</p>
      <ul>
        <li>Bug 的报告人和报告时间。</li>
        <li>Bug 的修改时间。</li>
        <li>Bug 的评论和更多详细信息。</li>
      </ul>
    </div>

    <div class="analysis-section">
      <h2 class="section-title">4. 思维导图</h2>
      <img src="../assets/imgs/BugZillaAnalysis.jpg" alt="思维导图" class="mindmap"/>
    </div>
  </el-card>
</template>

<script setup>
import { ElCard } from "element-plus";
import "element-plus/dist/index.css";
</script>

<style scoped>
.el-card {
  background-color: #f9f9f9;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
}

.el-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.header-title {
  color: #333;
  font-size: 24px;
  text-align: center;
  font-weight: bold;
  margin: 0;
}

.analysis-section {
  margin-bottom: 30px;
  padding: 10px;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.5s ease-in-out;
}

.section-title {
  color: #4caf50;
  font-size: 20px;
  border-bottom: 2px solid #4caf50;
  padding-bottom: 5px;
}

.feature {
  color: #ff5722;
}

ul {
  padding-left: 20px;
}

ul li {
  margin-bottom: 10px;
}

.mindmap {
  width: 100%;
  height: auto;
  margin-top: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
