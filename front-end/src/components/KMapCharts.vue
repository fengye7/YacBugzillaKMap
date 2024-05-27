<template>
  <el-container
    v-loading="loading"
    element-loading-text="Loading..."
    fullscreen
  >
    <div id="KMapChart" class="k-map-chart"></div>
    <div>
      <el-input
        v-model="competitorDomains"
        placeholder="输入竞争公司域名, 以逗号分隔"
        style="margin-bottom: 20px"
      ></el-input>
      <el-button @click="fetchData">获取数据</el-button>
    </div>
  </el-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getKMapData } from "@/api/KMapAPI.js";
import * as echarts from "echarts";

const seriesData = ref([]);
const seriesLinks = ref([]);
const categories = ref([
  { name: "product" },
  { name: "component" },
  { name: "assignee" },
]);

const competitorDomains = ref("");
const loading = ref(false);

onMounted(() => {
  initKMapChart();
});

async function fetchData() {
  loading.value = true;
  try {
    const domains = competitorDomains.value
      .split(",")
      .map((domain) => domain.trim());
    const response = await getKMapData(domains);
    const kMapData = response.data;
    formatData(kMapData);
    initKMapChart();
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    loading.value = false;
  }
}

function formatData(data) {
  seriesData.value = data.nodes;
  seriesLinks.value = data.links;
}

function initKMapChart() {
  const chartDom = document.getElementById("KMapChart");
  const myChart = echarts.init(chartDom);
  const option = {
    animationDurationUpdate: 500,
    animationEasingUpdate: "quinticInOut",
    tooltip: {
      show: true,
    },
    series: [
      {
        type: "graph",
        layout: "force",
        data: seriesData.value,
        links: seriesLinks.value,
        categories: categories.value,
        roam: true,
        label: {
          position: "right",
          formatter: "{b}",
        },
        lineStyle: {
          color: "source",
          curveness: 0.3,
        },
        emphasis: {
          focus: "adjacency",
          lineStyle: {
            width: 10,
          },
        },
        legendHoverLink: true, //是否启用图例 hover(悬停) 时的联动高亮。
        hoverAnimation: true, //是否开启鼠标悬停节点的显示动画
        focusNodeAdjacency: true,
        edgeSymbol: ["", "arrow"],
        force: {
          edgeLength: 15,
          repulsion: 200,
        },
        draggable: true, //每个节点的拖拉
        itemStyle: {
          emphasis: {
            //鼠标放上去有阴影效果
            shadowColor: "#00FAE1",
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowBlur: 40,
          },
        },
      },
    ],
  };

  myChart.setOption(option);
}
</script>

<style scoped>
.k-map-chart {
  height: 80vh;
  width: 100%;
}
</style>
