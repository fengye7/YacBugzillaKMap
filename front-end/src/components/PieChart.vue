<template>
    <el-card>
        <div ref="chartRef" :style="{ width: '1000%', height: '600%' }"></div>
    </el-card>
</template>

<script setup>
import * as echarts from "echarts";
import { defineProps, ref, onMounted, watch } from "vue";
import axios from 'axios';

//axios
const data = ref({});

let baseUrl = 'http://47.120.41.97:8002/bugs/'

const fetchData = async () => {
    try {
        const response = await axios.get(baseUrl + 'companies');
        data.value = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
        if (chart) {
            chart.setOption(getOption());
        }
        console.log(data)
        console.log(data.value)
        console.log(chart)
        console.log(chart.value)

    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

//initiate of pie chart
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

const chartRef = ref(null);

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
        title: {
            text: '企业数量统计',
            subtext: '按提交人邮箱后缀统计',
            // left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20
        },
        series: [
            {
                name: '占比',
                type: 'pie',
                radius: '80%',
                // data: data.value.map(item => ({
                //     value: item.value,
                //     name: item.name
                // })),
                data: Object.entries(data.value).map(([name, value]) => ({ name, value })),
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
};

const initChart = () => {
    fetchData();
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
};

</script>