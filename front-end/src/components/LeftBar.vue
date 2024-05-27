<template>
    <!-- <el-tabs tab-position="left" class="demo-tabs"> -->
    <el-tabs tab-position="left">
        <el-tab-pane label="折线图">
            <LineChart :data="chartData" />
        </el-tab-pane>
        <el-tab-pane label="柱状图">
            <BarChart :data="chartData" />
        </el-tab-pane>
        <el-tab-pane label="饼图">
            <PieChart/>
        </el-tab-pane>
        <el-tab-pane label="散点图">
            <ScatterChart/>
        </el-tab-pane>
        <el-tab-pane label="789">Task</el-tab-pane>
        <el-tab-pane label="666">Task</el-tab-pane>
        <el-tab-pane label="哈哈哈">Task</el-tab-pane>
    </el-tabs>
</template>

<script setup>
import LineChart from '../components/LineChart.vue';
import BarChart from '../components/BarChart.vue';
import PieChart from '../components/PieChart.vue';
import ScatterChart from '../components/ScatterChart.vue';

const chartData = [
    { date: '2023-01-01', value: 100 },
    { date: '2023-01-02', value: 150 },
    { date: '2023-01-03', value: 200 },
    // 更多数据...
];

</script>

<style>
.demo-tabs>.el-tabs__content {
    padding: 32px;
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
}

.el-tabs--right .el-tabs__content,
.el-tabs--left .el-tabs__content {
    height: 100%;
}
</style>