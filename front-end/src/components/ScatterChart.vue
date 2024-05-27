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
        },
        yAxis: {
        },
        series: [
            {
                symbolSize: 20,
                data: [
                    [10.0, 8.04],
                    [8.07, 6.95],
                    [13.0, 7.58],
                    [9.05, 8.81],
                    [11.0, 8.33],
                    [14.0, 7.66],
                    [13.4, 6.81],
                    [10.0, 6.33],
                    [14.0, 8.96],
                    [12.5, 6.82],
                    [9.15, 7.2],
                    [11.5, 7.2],
                    [3.03, 4.23],
                    [12.2, 7.83],
                    [2.02, 4.47],
                    [1.05, 3.33],
                    [4.05, 4.96],
                    [6.03, 7.24],
                    [12.0, 6.26],
                    [12.0, 8.84],
                    [7.08, 5.82],
                    [5.02, 5.68]
                ],
                type: 'scatter'
            }
        ]
    };
};

const initChart = () => {
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
};

</script>