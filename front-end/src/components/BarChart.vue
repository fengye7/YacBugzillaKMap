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
                type: 'bar'
            }
        ]
    };
};

const initChart = () => {
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
};

</script>