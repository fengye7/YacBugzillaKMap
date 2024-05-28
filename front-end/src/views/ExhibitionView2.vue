<template>  
    <el-container>  
      <el-aside width="200px">  
        <el-collapse v-model="activeNames" accordion>  
          <!-- 一级导航：始终展开的Product -->  
          <el-collapse-item title="Product" name="Product">  
            <!-- 二级导航：具体的product值 -->  
            <el-collapse-item  
              v-for="(product, index) in uniqueProducts"  
              :key="index"  
              :title="product"  
              :name="product"  
              @click="handleCollapseItemClick(product)"  
            >  
              <!-- 这里不需要子菜单 -->  
            </el-collapse-item>  
          </el-collapse-item>  
        </el-collapse>  
      </el-aside>  
    
      <el-main>  
        <el-card class="box-card">  
          <el-table  
            :data="filteredBugs"  
            style="width: 100%"  
          >  
          <el-table-column  
            prop="id"  
            label="ID"  
          ></el-table-column>  
          <el-table-column  
            prop="product"  
            label="Product"  
          ></el-table-column>  
          <el-table-column  
            prop="version"  
            label="Version"  
          ></el-table-column> 
          
          </el-table>  
        </el-card>  
      </el-main>  
    </el-container>  
  </template>  
    
  <script>  
  import { ref, computed/*, watch*/ } from 'vue';  
    
  export default {  
    name: 'BugList',  
    setup() {  
        const bugs = ref([  
      // 示例数据  
      { id: 1, status: 'NEW', version: '1.0', component: 'UI', summary: 'Bug summary 1', product: 'product1' },  
      { id: 2, status: 'ASSIGNED', version: '1.1', component: 'API', summary: 'Bug summary 2', product: 'product2' },  
      // ... 其他bug数据  
    ]);  
      // 不需要activeNames来追踪二级导航的激活状态，因为所有二级都是可点击的  
      // 但是我们需要一个变量来存储当前选中的product以进行筛选  
      const selectedProduct = ref('');  
    
      // 计算唯一的product列表  
      const uniqueProducts = computed(() => {  
        return [...new Set(bugs.value.map(bug => bug.product))];  
      });  
    
      // 计算筛选后的bug列表  
      const filteredBugs = computed(() => {  
        return bugs.value.filter(bug => bug.product === selectedProduct.value);  
      });  
    
      // 处理二级导航点击事件  
      const handleCollapseItemClick = (product) => {  
        selectedProduct.value = product;  
      };  
    
      // 监听selectedProduct的变化，如果有必要，可以发送请求或执行其他操作  
      /*watch(selectedProduct, (newVal) => {  
        // ...额外的逻辑...  
      }, { immediate: false });  */
    
      return {  
        bugs,  
        uniqueProducts,  
        filteredBugs,  
        handleCollapseItemClick,  
      };  
    },  
  };  
  </script>  
    
  <style scoped>  
  .el-collapse-item__header {  
  font-size: 14px;  
  color: #606266;  
  background-color: #f5f7fa;  
  border-bottom: 1px solid #ebeef5;  
  border-radius: 4px 4px 0 0;  
  cursor: pointer;  
  padding: 10px 15px;  
  position: relative;  
  transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);  
  }  
  
  .box-card {  
  margin-bottom: 20px;  
  }  
  </style>