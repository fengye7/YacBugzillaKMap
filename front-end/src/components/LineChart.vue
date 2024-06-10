<template>
    <el-card>
        <div ref="chartRef" :style="{ width: '1000%', height: '600%' }"></div>
    </el-card>
</template>

<script setup>
import * as echarts from "echarts";
import { defineProps, ref, onMounted, watch } from "vue";
// import axios from 'axios';

//axios
// const data = ref({});
const chartRef = ref(null);

// let baseUrl = 'http://47.120.41.97:8002/bugs/'

// const fetchData = async () => {
//     try {
//         const response = await axios.get(baseUrl + 'statuses');
//         chartRef.value = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
//         if (chart) {
//             chart.setOption(getOption());
//         }
//     } catch (error) {
//         console.error('Error fetching data:', error);
//     }
// };

const props = defineProps({
    data: {
        type: Array,
        required: true
    },
    xAxisDataKey: {
        type: String,
        default: 'date'
    },
    yAxisDataKey: {
        type: String,
        default: 'value'
    }
});

onMounted(() => {
    initChart();
});

watch(
    () => props.data,
    () => {
        if (chart) {
            chart.setOption(getOption());
        }
    },
    { deep: true }
);

let chart;

const getOption = () => {
    return {
        xAxis: {
            type: 'category',
            data: props.data.map(item => item[props.xAxisDataKey])
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: props.data.map(item => item[props.yAxisDataKey]),
                type: 'line'
            }
        ]
    };
};

const initChart = () => {
    // fetchData();
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
};

</script>