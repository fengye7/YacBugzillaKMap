<template>
    <el-progress :percentage="percentage" :stroke-width="15" striped striped-flow />
    <el-card>
        <div ref="chartRef" :style="{ width: '100%', height: '600%' }"></div>
    </el-card>
</template>

<script setup>
import * as echarts from "echarts";
import { ref, onMounted } from "vue";
// import { defineProps, ref, onMounted, watch } from "vue";
import axios from 'axios';

let chart;

const percentage = ref(10)

//axios
const sev = ref(null);
const chartRef = ref([]);
let option = {
    title: {
        text: '状态-严重性堆叠条形图',
        subtext: '按状态聚类统计',
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
        }
    },
    legend: {},
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value'
    },
    yAxis: {
        type: 'category',
        data: []
    },
    series: [
        // {
        //     name: 'Search Engine',
        //     type: 'bar',
        //     stack: 'total',
        //     label: {
        //         show: true
        //     },
        //     emphasis: {
        //         focus: 'series'
        //     },
        //     data: [820, 832, 901, 934, 1290, 1330, 1320]
        // }
    ]
};

let baseUrl = 'http://47.120.41.97:8002/bugs/'

const fetchRef = async () => {
    try {
        const response = await axios.get(baseUrl + 'statuses');
        // chartRef = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
        chartRef.value = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
        if (chart) {
            chart.setOption(getOption());
        }

        console.log('chartRefvalue', chartRef.value)

    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const fetchSev = async () => {
    try {
        const response = await axios.get(baseUrl + 'severity');
        // sev = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
        sev.value = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构

        console.log('severity', sev)

    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const fetchData = async () => {
    // for (var sta in chartRef.value) {
    await fetchRef();
    await fetchSev();

    for (var i = 0; i < sev.value.length; i++) {
        option.series.push({
            name: sev.value[i],
            type: 'bar',
            stack: 'Ad',
            label: { show: true },
            emphasis: { focus: 'series' },
            data: []
        });
        console.log('666666', sev.value[i])
        console.log('option.series', option.series)
        for (var j = 0; j < chartRef.value.length; j++) {
            await axios.get(baseUrl + 'severityStatusCount', {
                params: {
                    status: chartRef.value[j],
                    severity: sev.value[i],
                }
            }).then(response => {
                console.log(response.data.count);
                // 处理成功的情况
                option.series[option.series.length - 1].data.push(response.data.count);

            })
                .catch(error => {
                    // 处理错误情况
                    console.error('Error fetching data:', error);
                });
        }

        percentage.value = (i + 1) * 100 / sev.value.length
        if (percentage.value > 100) {
            percentage.value = 100
        }

        if (chart) {
            option.yAxis.data = chartRef.value
            chart.setOption(getOption());
            console.log(option)
        }
    }

};

onMounted(() => {
    initChart();
});

const getOption = () => {
    return option;
};

const initChart = () => {

    // fetchRef();
    // console.log('a')
    // fetchSev();
    // console.log('d')
    fetchData();
    console.log('e')
    chart = echarts.init(chartRef.value);
    console.log('b')
    chart.setOption(getOption());
    console.log('c')
};

</script>