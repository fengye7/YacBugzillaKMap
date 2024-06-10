# 项目配置教程

# 前置准备

pip/python环境

![image](https://github.com/fengye7/YacBugzillaKMap/assets/117179005/33ef4d8d-a644-4333-a68f-11b527587ab0)


node.js环境

![image](https://github.com/fengye7/YacBugzillaKMap/assets/117179005/45b48ad1-75cc-43ba-a3e9-a4fc4d3d1f1b)


## 配置后端

[超详细Django+vue+vscode前后端分离搭建_vscode django vue-CSDN博客](https://blog.csdn.net/weixin_43883625/article/details/130190149)

- 使用项目只需要安装一定的依赖项：

使用venv环境，初始pip list为空

- 首先需要: ```pip install django```

- 使用pysql: ```pip install pymysql```

- django rest framework:
```sh
pip install djangorestframework
# 暂时不装也可以
pip install markdown
# 用于数据筛选
pip install django-filter
```

-api文档swagger: ```pip install drf-yasg```

-前后端联调——利用django-cors-headers模块[解决跨域问题](https://so.csdn.net/so/search?q=%E8%A7%A3%E5%86%B3%E8%B7%A8%E5%9F%9F%E9%97%AE%E9%A2%98&spm=1001.2101.3001.7020)

```sh
pip install django-cors-headers
```
![image](https://github.com/fengye7/YacBugzillaKMap/assets/117179005/f5a211b5-076e-46d1-affd-339bb460f061)



## 配置前端

```sh
npm install -g @vue/cli
```

![image](https://github.com/fengye7/YacBugzillaKMap/assets/117179005/4bb47fcc-5256-4f9e-9f7b-9b38e8522045)

```sh
npm install axios 
npm install element-plus --save
```

## 使用仓库
***git pull***在每次push之前是必要的

## 运行项目
**后端**
```sh
python manage.py runserver
```

**前端**

生成图形界面控制
```sh
vue ui
```
直接命令行
```sh
npm run serve 或 vue serve
```
