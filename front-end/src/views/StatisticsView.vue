<template>
    <div class="common-layout">
        <el-container>
            <el-aside width="200px">
                <LeftBar />
            </el-aside>
            <el-main>
                <router-view />
            </el-main>
        </el-container>
    </div>
</template>

<script setup>
import LeftBar from '../components/LeftBar.vue';

</script>