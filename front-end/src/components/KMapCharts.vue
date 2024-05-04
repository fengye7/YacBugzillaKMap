<template>
  <el-container><div id="KMapChart" class="k-map-chart"></div>
   <div>
    <button @click="fetchData">Fetch Data</button>
    <div v-if="testdata">
      <p>{{ testdata }}</p>
    </div>
  </div>
  </el-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
var echarts = require("echarts/lib/echarts");
require("echarts/lib/chart/graph");
require("echarts/lib/component/tooltip");
require("echarts/lib/component/title");

import "../mock/KMapMock";
import { MockAPI } from "@/utils/request";
let KMapChart = null;
let kMapData = {};
const seriesData = ref([]);
const seriesLinks = ref([]);
const categories = ref([]);
// const lastClickId = ref("");
const colors = [
  "#a3d2ca",
  "#056676",
  "#ea2c62",
  "#16a596",
  "#03c4a1",
  "#f5a25d",
  "#8CD282",
  "#32e0c4",
  "#00FAE1",
  "#f05454",
];

onMounted(async () => {
  await initKMapData();
  console.log("完成init", kMapData);
  formatData(kMapData);

  initKMapChart(); // 调用渲染函数
});

let testdata = ref(null);
import {getKMapData} from '@/api/KMapAPI.js'
async function fetchData() {
      try {
        testdata = await getKMapData();
        console.log(testdata);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

/**
 * 初始化图表数据
 */
async function initKMapData() {
  return new Promise((resolve, reject) => {
    MockAPI.get("kMap/getKMapDataMock")
      .then((res) => {
        kMapData = res.data.dataset;
        resolve(); // 请求成功后调用 resolve
      })
      .catch((error) => {
        reject(error); // 请求失败时调用 reject
      });
  });
}

/**
 * 节点点击事件
 */
async function nodeClick(params) {
  const index = seriesData.value.findIndex(
    (item) => item.id === params.data.id
  );
  console.log("点了节点：" + (index + 1), "clicked");
}

/**
 * 设置echarts配置项,重绘画布
 */
async function initKMapChart() {
  if (!KMapChart) {
    console.log("KMapChart开始初始化");
    KMapChart = echarts.init(document.getElementById("KMapChart"));
    KMapChart.on("click", (params) => {
      if (params.dataType === "node") {
        nodeClick(params); //判断点击的是图表的节点部分
      }
    });
  }
  // 指定图表的配置项和数据
  let option = {
    animationDurationUpdate: 500, // 动画更新变化时间
    animationEasingUpdate: "quinticInOut",
    tooltip: {
      show: false,
    },
    series: [
      {
        type: "graph",
        layout: "force",
        legendHoverLink: true, //是否启用图例 hover(悬停) 时的联动高亮。
        hoverAnimation: true, //是否开启鼠标悬停节点的显示动画
        focusNodeAdjacency: true,
        edgeLabel: {
          position: "middle", //边上的文字样式
          normal: {
            show: true,
            textStyle: {
              fontSize: 12,
            },
            position: "middle",
            formatter: function (x) {
              return x.data.name;
            },
          },
        },
        edgeSymbol: ["", "arrow"],
        force: {
          edgeLength: 15,
          repulsion: 200,
        },
        roam: true,
        draggable: true, //每个节点的拖拉
        itemStyle: {
          normal: {
            color: "#00FAE1",
            cursor: "pointer",
            label: {
              show: true,
              position: [-10, -15],
              textStyle: {
                //标签的字体样式
                color: "#AB8", //字体颜色
                fontStyle: "normal", //文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                fontWeight: "bold", //'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                fontFamily: "sans-serif", //文字的字体系列
                fontSize: 12, //字体大小
              },
            },
            nodeStyle: {
              brushType: "both",
              borderColor: "rgba(255,215,0,0.4)",
              borderWidth: 1,
            },
          },
          emphasis: {
            //鼠标放上去有阴影效果
            shadowColor: "#00FAE1",
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowBlur: 40,
          },
        },
        lineStyle: {
          width: 2,
        },
        label: {
          fontSize: 18,
        },
        symbolSize: 24, //节点大小
        links: seriesLinks.value,
        data: seriesData.value,
        categories: categories.value,
        cursor: "pointer",
      },
    ],
  };
  // 使用刚指定的配置项和数据显示图表。
  KMapChart.setOption(option);
}

/**
 * 格式化数据到表格需要的数据
 */
function formatData(list) {
  let nodes = list.nodes;
  let links = list.links;
  console.log("nodes:", nodes);
  console.log("links:", links);

  let colorIndex = 0;
  let loadedCat = [];
  nodes.forEach((item) => {
    if (item.categary && loadedCat.indexOf(item.categary) === -1) {
      colorIndex = Math.floor(Math.random() * colors.length);
      loadedCat.push(item.categary);
      categories.value.push({ name: item.categary });
    }
    item.itemStyle = {
      color: colors[colorIndex],
      borderColor: "#ffffff",
    };
    seriesData.value.push(item);
  });
  links.forEach((item) => {
    seriesLinks.value.push(item);
  });
  console.log("seriesData:", seriesData.value);
  console.log("seriesLinks:", seriesLinks.value);
}
</script>

<style scoped>
.k-map-chart {
  height: 80vh;
  width: 100%;
}
</style>