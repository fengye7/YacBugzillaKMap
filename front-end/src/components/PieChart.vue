<template>
    <el-card>
        <div ref="chartRef" :style="{ width: '1000%', height: '600%' }"></div>
    </el-card>
</template>

<script setup>
import * as echarts from "echarts";
import { defineProps, ref, onMounted, watch } from "vue";

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
            text: 'Referer of a Website',
            subtext: 'Fake Data',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [
            {
                name: 'Access From',
                type: 'pie',
                radius: '50%',
                data: [
                    { value: 1048, name: 'Search Engine' },
                    { value: 735, name: 'Direct' },
                    { value: 580, name: 'Email' },
                    { value: 484, name: 'Union Ads' },
                    { value: 300, name: 'Video Ads' }
                ],
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
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
};

</script>