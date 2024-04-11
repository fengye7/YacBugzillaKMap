import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import axios from './utils/request.js'

const app = createApp(App)
app.use(ElementPlus)
app.use(store)
app.use(router)

app.mount('#app')
app.config.globalProperties.$axios=axios;  //配置axios的全局引用