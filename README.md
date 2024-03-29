# 项目配置教程

# 前置准备

pip/python环境

![image](https://github.com/fengye7/YacBugzillaKmap/assets/117179005/14f4f76b-13fd-4ec2-aa80-0bd1981d1256)

node.js环境

![image](https://github.com/fengye7/YacBugzillaKmap/assets/117179005/3a441335-2501-43da-bca6-0d4ac48cbe36)

## 配置后端

[超详细Django+vue+vscode前后端分离搭建_vscode django vue-CSDN博客](https://blog.csdn.net/weixin_43883625/article/details/130190149)

- 使用项目只需要安装一定的依赖项：

使用venv环境，初始pip list为空

-首先需要: pip install django

-使用pysql: pip install pymysql

-django rest framework: 

```cpp
pip install djangorestframework
# 暂时不装也可以
pip install markdown
# 用于数据筛选
pip install django-filter
```

-api文档swagger:   pip install drf-yasg

-前后端联调——利用django-cors-headers模块[解决跨域问题](https://so.csdn.net/so/search?q=%E8%A7%A3%E5%86%B3%E8%B7%A8%E5%9F%9F%E9%97%AE%E9%A2%98&spm=1001.2101.3001.7020)

```bash
pip install django-cors-headers
```
![image](https://github.com/fengye7/YacBugzillaKmap/assets/117179005/4c7b9b62-b24b-40c1-891e-a93eafff3e50)


## 配置前端

npm install -g @vue/cli

![image](https://github.com/fengye7/YacBugzillaKmap/assets/117179005/76572e3c-4fff-46cd-b8d5-5b7d5c5a857c)

npm install axios 

npm install element-plus --save
