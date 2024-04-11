/**
 * 图谱数据源源
 */
import Mock from 'mockjs'  //导入mockjs

//使用Mock下面提供的mock方法进行需要模拟数据的封装
//参数1，是需要拦截的完整请求地址，参数2，是请求方式，参数3，是请求的模拟数据

Mock.mock('/getKMapData', 'get', {
    status:200, //请求成功状态码
    dataset:{
        nodes: [
            {
                id:1,
                name:'测试节点',
                categary:'1',
                symbolSize: 60
            },
            {
                id:2,
                name:'测试节点',
                categary:'1',
                symbolSize: 40
            },
            {
                id:3,
                name:'测试节点',
                categary:'2',
            },
            {
                id:4,
                name:'测试节点',
                categary:'',
            },
            {
                id:5,
                name:'测试节点测试节点',
                categary:'',
            },
            {
                id:6,
                name:'测试节点',
                categary:'2',
            },
            {
                id:7,
                name:'测试节点',
                categary:'',
            },
            {
                id:8,
                name:'测试节点',
                categary:'',
            },
            {
                id:9,
                name:'测试节点',
                categary:'',
            },
            {
                id:10,
                name:'测试节点',
                categary:'',
            }
        ],
        links: [
            {source: '2', target: '3', name: ''},
            {source: '3', target: '4', name: ''},
            {source: '3', target: '5', name: ''},
            {source: '5', target: '6', name: ''},
            {source: '5', target: '7', name: ''},
            {source: '5', target: '8', name: ''},
            {source: '9', target: '10', name: ''},
            {source: '10', target: '9', name: ''},
            {source: '1', target: '2' , name: ''},
            {source: '1', target: '10', name: ''}
            
        ]
    }
    })

