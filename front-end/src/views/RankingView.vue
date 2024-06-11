<template>
  <div class="search-component">
    <h2>热度搜索</h2>
    <p>选择搜索模式并输入数量或天数，然后点击搜索按钮，查看Product和Component热度。</p>
    <div class="form-group">
      <label for="mode">搜索模式：</label>
      <select v-model="selectedMode" id="mode" class="input-field">
        <option value="reported">Bug上报</option>
        <option value="modified">Bug修改</option>
        <option value="commented">Bug评论</option>
      </select>
    </div>
    <div class="form-group">
      <label for="type">搜索方法：</label>
      <select v-model="searchType" id="type" class="input-field">
        <option value="count">按数量</option>
        <option value="days">按时间范围</option>
      </select>
    </div>
    <div class="form-group" v-if="searchType === 'count'">
      <label for="n">数量（最新n个）：</label>
      <input type="number" v-model="n" id="n" min="1" class="input-field">
    </div>
    <div class="form-group" v-if="searchType === 'days'">
      <label for="days">时间范围（近n天）：</label>
      <input type="number" v-model="days" id="days" min="1" class="input-field">
    </div>
    <button @click="search" class="search-button">搜索</button>
    <button @click="exportToExcel" class="export-button" v-if="productResults && componentResults">导出为Excel</button>
    <div v-if="productResults !== null && componentResults !== null" class="results">
      <div class="column">
        <h3>Product热度</h3>
        <ul v-if="productResults.length > 0">
          <li v-for="result in productResults" :key="result.product || result.component">
            {{ result.product || result.component }}: {{ result.count }}
          </li>
        </ul>
        <p v-else>没有找到相关的Product数据。</p>
      </div>
      <div class="column">
        <h3>Component热度</h3>
        <ul v-if="componentResults.length > 0">
          <li v-for="result in componentResults" :key="result.product || result.component">
            {{ result.component || result.product }}: {{ result.count }}
          </li>
        </ul>
        <p v-else>没有找到相关的Component数据。</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import * as XLSX from 'xlsx';

const selectedMode = ref('reported');
const searchType = ref('count');
const n = ref(1);
const days = ref(1);
const productResults = ref(null);
const componentResults = ref(null);
const baseURL = process.env.VUE_APP_BASE_URL;

const search = async () => {
  try {
    let productResponse;
    let componentResponse;

    if (searchType.value === 'count') {
      if (selectedMode.value === 'reported') {
        productResponse = await axios.get(`${baseURL}/rankings/latest_reported_products/${n.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/latest_reported_components/${n.value}/`);
      } else if (selectedMode.value === 'modified') {
        productResponse = await axios.get(`${baseURL}/rankings/latest_modified_products/${n.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/latest_modified_components/${n.value}/`);
      } else if (selectedMode.value === 'commented') {
        productResponse = await axios.get(`${baseURL}/rankings/latest_commented_products/${n.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/latest_commented_components/${n.value}/`);
      }
    } else if (searchType.value === 'days') {
      if (selectedMode.value === 'reported') {
        productResponse = await axios.get(`${baseURL}/rankings/reported_products_by_days/${days.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/reported_components_by_days/${days.value}/`);
      } else if (selectedMode.value === 'modified') {
        productResponse = await axios.get(`${baseURL}/rankings/modified_products_by_days/${days.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/modified_components_by_days/${days.value}/`);
      } else if (selectedMode.value === 'commented') {
        productResponse = await axios.get(`${baseURL}/rankings/commented_products_by_days/${days.value}/`);
        componentResponse = await axios.get(`${baseURL}/rankings/commented_components_by_days/${days.value}/`);
      }
    }

    productResults.value = productResponse.data;
    componentResults.value = componentResponse.data;
  } catch (error) {
    console.error("获取数据时出错:", error);
    productResults.value = [];
    componentResults.value = [];
  }
};

const exportToExcel = () => {
  const productData = productResults.value.map(item => ({ 名称: item.product, 数量: item.count }));
  const componentData = componentResults.value.map(item => ({ 名称: item.component, 数量: item.count }));

  const wsProduct = XLSX.utils.json_to_sheet(productData);
  const wsComponent = XLSX.utils.json_to_sheet(componentData);

  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, wsProduct, 'Product 热度');
  XLSX.utils.book_append_sheet(wb, wsComponent, 'Component 热度');

  XLSX.writeFile(wb, '热度结果.xlsx');
};
</script>

<style scoped>
.search-component {
  font-size: 18px;
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.search-component h2 {
  font-size: 24px;
  text-align: center;
  color: #333;
}

.search-component p {
  text-align: center;
  color: #555;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

.input-field {
  width: 100%;
  padding: 12px;
  font-size: 18px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.search-button, .export-button {
  display: block;
  width: 100%;
  padding: 12px;
  font-size: 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

.search-button:hover, .export-button:hover {
  background-color: #0056b3;
}

.results {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.column {
  width: 45%;
}

.results h3 {
  text-align: center;
  color: #333;
}

.results ul {
  list-style: none;
  padding: 0;
}

.results li {
  background-color: #f1f1f1;
  margin: 5px 0;
  padding: 10px;
  border-radius: 4px;
}
</style>
