<template>
    <el-menu v-model="currentComponent" default-active="line" class="el-menu-demo" mode="vertical"
        @select="handleSelect">
        <el-menu-item index="pie">企业数量统计</el-menu-item>
        <el-menu-item index="bar">状态-严重性图</el-menu-item>
        <el-menu-item index="bar2">状态-优先级图</el-menu-item>
    </el-menu>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from "vue-router";
// import { ref, defineAsyncComponent, onMounted } from 'vue';
// import ElTabs from 'element-plus/es/components/tabs';
// import ElTabPane from 'element-plus/es/components/tab-pane';
// import LineChart from '../components/LineChart.vue';
// import BarChart from '../components/BarChart.vue';
// import PieChart from '../components/PieChart.vue';
// import ScatterChart from '../components/ScatterChart.vue';

// const chartData = [
//     { date: '2023-01-01', value: 100 },
//     { date: '2023-01-02', value: 150 },
//     { date: '2023-01-03', value: 200 },
//     // 更多数据...
// ];

// const Tab1 = defineAsyncComponent(() => import('../components/LineChart.vue'));
// const Tab2 = defineAsyncComponent(() => import('../components/BarChart.vue'));
// const Tab3 = defineAsyncComponent(() => import('../components/PieChart.vue'));
// const Tab4 = defineAsyncComponent(() => import('../components/ScatterChart.vue'));

// const tabs = [
//     { label: 'Bug数量随时间增长图', name: 'Tab1' },
//     { label: '状态-严重性图', name: 'Tab2' },
//     { label: '企业数量统计', name: 'Tab3' },
//     { label: 'Tab 2', name: 'Tab4' },
// ];

const currentComponent = ref('pie');
const router = useRouter();

const handleSelect = (index) => {
    // if (key === 'Tab1') {
    //     currentComponent.value = Tab1;
    // } else if (key === 'Tab2') {
    //     currentComponent.value = Tab2;
    // } else if (key === 'Tab3') {
    //     currentComponent.value = Tab3;
    // } else if (key === 'Tab4') {
    //     currentComponent.value = Tab4;
    // }
    currentComponent.value = index
    router.push({ path: `/statistics/${index}` }); // 路由跳转
};

// onMounted(() => {
//     handleSelect(tabs[0].name); // 默认加载第一个菜单项对应的组件
// });

// onMounted(() => {
//     loadComponent(activeName);
// });

// function loadComponent(componentName) {
//     if (componentName === 'Tab1') {
//         currentComponent = Tab1;
//         activeName = 'Tab1';
//     } else if (componentName === 'Tab2') {
//         currentComponent = Tab2;
//         activeName = 'Tab2';
//     } else if (componentName === 'Tab3') {
//         currentComponent = Tab3;
//         activeName = 'Tab3';
//     } else if (componentName === 'Tab4') {
//         currentComponent = Tab4;
//         activeName = 'Tab4';
//     }
// }
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