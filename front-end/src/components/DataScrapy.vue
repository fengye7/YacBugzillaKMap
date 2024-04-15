<template>
    <div id="sc" class="data-scrapy" :style="{ width: this.width, height: this.height }">
        <el-button type="primary" @click="onAddItem">数据爬取</el-button>
        <el-divider />
        <el-card style="height: 600px; margin-bottom: 0px; width:auto; margin-left: 50px;margin-right: 50px;">
            <el-table :data="tableData" stripe max-height="560" table-layout="auto" style="width: 100%">
                <el-table-column sortable align="center" prop="date" label="Date" width="180" />
                <el-table-column sortable align="center" prop="name" label="Name" width="180" />
                <el-table-column sortable align="center" prop="address" label="Address" />
            </el-table>
        </el-card>
    </div>
</template>

<script setup>
import { ElTable, ElButton, ElCard } from 'element-plus';
import { ref } from 'vue'

const now = new Date('2024-4-15')

const onAddItem = () => {
    now.setDate(now.getDate() + 1)
    tableData.value.push({
        date: now,
        name: Math.random(),
        address: Math.random(),
    })
}

const tableData = ref([
    {
        date: '2016-05-03',
        name: '666',
        address: '同济大学嘉定校区',
    },
    {
        date: '2016-05-02',
        name: 'B',
        address: '杨浦区四平路1239号',
    },
    {
        date: '2016-05-04',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
    },
    {
        date: '2016-05-01',
        name: 'C',
        address: '火星',
    },
])
</script>