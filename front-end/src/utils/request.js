//axiosInstance.js
//导入axios
import axios from 'axios'

//使用axios下面的create([config])方法创建axios实例
//导出我们建立的axios实例模块，ES6 export用法
export const API = axios.create({
	baseURL:'http://127.0.0.1:8000', //请求后端数据的基本地址，自定义
	timeout: 2000                   //请求超时设置，单位ms
})


export const MockAPI = axios.create({
	baseURL:'http://localhost:8080', //请求后端数据的基本地址，自定义
	timeout: 2000                   //请求超时设置，单位ms
})
