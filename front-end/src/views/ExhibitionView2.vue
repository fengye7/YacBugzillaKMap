<template>  
  <el-container>  
    <el-aside width="200px">  
      <!--侧边栏-->
      <el-collapse v-model="activeNames">  
        <el-collapse-item title="Status" name="status">  
          <div v-for="(bug, index) in uniqueValues('status')" :key="index">  
            <span class="filter-tag" @click="filterBy('status', bug)">{{ bug }}</span>  
          </div>  
        </el-collapse-item>  
        <el-collapse-item title="Version" name="version">  
          <div v-for="(bug, index) in uniqueValues('version')" :key="index">  
            <span class="filter-tag" @click="filterBy('version', bug)">{{ bug }}</span>  
          </div>  
        </el-collapse-item>  
        <el-collapse-item title="Product" name="product">  
          <div v-for="(product, index) in uniqueValues('product')" :key="index">  
            <span class="filter-tag" @click="filterBy('product', product)">{{ product }}</span>  
          </div>  
        </el-collapse-item>  
        <el-collapse-item title="Component" name="component">  
          <div v-for="(component, index) in uniqueValues('component')" :key="index">  
            <span class="filter-tag" @click="filterBy('component', component)">{{ component }}</span>  
          </div>  
        </el-collapse-item>  
      </el-collapse>  
    </el-aside>  
    <el-main>  
      <!--展览页（未替换为BugItem）-->
      <h2>Filtered Bugs</h2>  
      <el-card v-for="bug in filteredBugs" :key="bug.id" class="bug-card"> 
        <div class="clearfix">  
          <span>{{ bug.id }}</span>  
        </div>  
        <div>  
          <p>Status: {{ bug.status }}</p>  
          <p>Version: {{ bug.version }}</p>  
          <p>Product: {{ bug.product }}</p>  
          <p>Component: {{ bug.component }}</p>  
        </div>  
      </el-card>
       <!--<el-card>
      <BugItem
          v-for="bug in filteredBugs"
          :key="bug.id"
          :id="bug.id"
          :status="bug.status"
          :summary="bug.summary"
          :version="bug.version"
          :product="bug.product"
          :component="bug.component"
          :cardWidth="'100%'"
          @bug-info="handleViewBugInfo"
        />
      </el-card>--> 
    </el-main>  
  </el-container>  
</template>  
  
<script>  
import { ref, computed } from 'vue';  
import { ElCollapse, ElCollapseItem, ElCard, ElContainer, ElAside, ElMain } from 'element-plus';  

import BugItem from '../components/BugItem.vue';
import { useRouter } from "vue-router";

const router = useRouter();

export default {  
  components: {  
    ElCollapse,  
    ElCollapseItem,  
    ElCard,  
    ElContainer,  
    ElAside,  
    ElMain  
  },  
  setup() {  
    const bugs = ref([  
      { id: 1, status: 'NEW', version: '1.0', product: 'Product A', component: 'Component 1',summary:'111' },  
      { id: 2, status: 'ASSIGNED', version: '1.1', product: 'Product A', component: 'Component 2',summary:'222' },  
      { id: 3, status: 'NEW', version: '1.1', product: 'Product B', component: 'Component 1',summary:'333' },   
    ]);  
  
    const activeNames = ref(['status']); // 默认展开Status  
  
    const selectedFilter = ref(null);  
  
    const filteredBugs = computed(() => {  //筛选逻辑
      if (!selectedFilter.value) return bugs.value;  
  
      const [filterKey, filterValue] = selectedFilter.value;  
      return bugs.value.filter(bug => bug[filterKey] === filterValue);  
    });  
  
    function filterBy(key, value) { //侧边栏触发筛选
      selectedFilter.value = [key, value];  
    }  
  
    function uniqueValues(prop) {  
      const values = new Set();  
      bugs.value.forEach(bug => values.add(bug[prop]));  
      return Array.from(values);  
    }  
    
    const handleViewBugInfo = (id) => {
      router.push({ name: 'bug-info', params: { id } });
    }
  
    return {  
      bugs,  
      activeNames,  
      filteredBugs,  
      filterBy,  
      uniqueValues,
      BugItem,
      handleViewBugInfo
    };  
  }  
};  
</script>

<style scope>

.filter-tag{
  font-size:12px;
  color: gray;
};

</style>