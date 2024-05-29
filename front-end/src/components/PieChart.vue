<template>
    <el-card>
        <div ref="chartRef" :style="{ width: '100%', height: '600%' }"></div>
    </el-card>

</template>

<script setup>
import * as echarts from "echarts";
// import { defineProps, ref, onMounted, watch } from "vue";
import { ref, onMounted } from "vue";
import axios from 'axios';

//axios
const data = ref({
    "windriver.com": 1033,
    "mvista.com": 211,
    "bigsur.com": 208,
    "intel.com": 2403,
    "linuxfoundat...": 798,
    "yoctoproject.org": 1035,
    "arm.com": 665,
    "linux.intel.com": 57,
    "circuitco.com": 3,
    "gmail.com": 1234,
    "bluelightning...": 344,
    "gherzan.com": 3,
    "ossystems.com.br": 38,
    "enea.com": 8,
    "linuxfoundation.org": 299,
    "ni.com": 162,
    "inte...": 22,
    "freescale.com": 16,
    "eaglescrag.net": 13,
    "linux.i...": 23,
    "intel...": 162,
    "timomueller.eu": 1,
    "pabigot.com": 1,
    "denix.org": 9,
    "verizon.com": 1,
    "holtmann.org": 4,
    "pbarker.dev": 4,
    "kernel.org": 4,
    "hitach...": 1,
    "enea.se": 1,
    "mail.de": 1,
    "linaro.org": 5,
    "rambler.ru": 1,
    "seebs.net": 17,
    "audiogeek.co.uk": 1,
    "anpa.de": 1,
    "technux.se": 2,
    "minimum.se": 2,
    "live.com": 2,
    "innoide.com": 1,
    "peter-eng.com.au": 1,
    "pld-linux.org": 1,
    "easyarm.com": 1,
    "goto.fi": 97,
    "nsn.com": 1,
    "embed.me.uk": 1,
    "juno.com": 1,
    "...": 129,
    "iki.fi": 3,
    "i...": 22,
    "timesys.com": 2,
    "octagonsystems.com": 1,
    "openedhand.com": 1,
    "coxtr.com": 1,
    "int...": 6,
    "balister.org": 2,
    "linux.intel...": 56,
    "kde.org": 1,
    "fake.user": 68,
    "konsulko.com": 112,
    "wanadoo.fr": 1,
    "gmx.de": 46,
    "tpip.net": 1,
    "nwlink.com": 1,
    "cetola.net": 68,
    "nxp.com": 2,
    "gmx.net": 1,
    "vector.com": 1,
    "mailbox.org": 1,
    "codethink...": 1,
    "andred.net": 3,
    "mlbassoc.com": 1,
    "imgtec.com": 1,
    "denx.de": 1,
    "ikusi.com": 1,
    "mender.io": 1,
    "seeingmachin...": 1,
    "mentor.com": 3,
    "pidge.org": 16,
    "converseincode.com": 2,
    "nathanrossi.com": 3,
    "qq.com": 2,
    "in...": 5,
    "huawei.com": 2,
    "happypunch.com": 3,
    "dev.rtsoft.ru": 1,
    "buzzcollectivemarket...": 20,
    "axis.com": 4,
    "deserted.net": 2,
    "op.pl": 1,
    "menlosystems.com": 1,
    "madison.systems": 4,
    "reliableembeddeds...": 10,
    "gmx.li": 1,
    "asterius.io": 3,
    "relysys.co.in": 1,
    "baslerweb.com": 1,
    "bmw.de": 2,
    "nonadev.net": 1,
    "xilinx.com": 17,
    "hcl.com": 8,
    "3mdeb.com": 2,
    "microch...": 1,
    "prsolucoes.com": 1,
    "dynamicdevices.co.uk": 1,
    "kdab.com": 1,
    "rsi-elektrotechnik.de": 1,
    "alibaba-inc.com": 1,
    "titv.se": 1,
    "gmai...": 1,
    "googlema...": 2,
    "siemens.com": 2,
    "aerq.com": 1,
    "kernel.crashing.org": 5,
    "stusta.de": 2,
    "free.fr": 3,
    "polysync.io": 1,
    "aox-tech.de": 1,
    "vanmierlo.com": 1,
    "ithinx.io": 1,
    "cybertrust.c...": 1,
    "enedino.org": 9,
    "sakoman.com": 28,
    "saye.org": 1,
    "ronell.me": 1,
    "126.com": 1,
    "hotmail.com": 2,
    "crashcourse.ca": 2,
    "evolware.org": 1,
    "bootlin.com": 124,
    "uwaterloo.ca": 9,
    "whitetree.xyz": 1,
    "amazon.com": 1,
    "scs.ch": 1,
    "cybernetics.com": 2,
    "taitradio.com": 1,
    "gma...": 1,
    "opensynergy.com": 2,
    "web.de": 1,
    "cookiesoft.de": 1,
    "richelberger.com": 3,
    "generac.com": 1,
    "neumann-web.eu": 1,
    "zhukoff.net": 43,
    "qt.io": 1,
    "microsoft.com": 2,
    "shaiton.org": 1,
    "amazon.de": 7,
    "welotec.com": 6,
    "majess.pl": 1,
    "in.bosch.com": 1,
    "nl.abb.com": 1,
    "smile.fr": 22,
    "kpit.com": 1,
    "st.com": 1,
    "renesas.com": 1,
    "baylibre.com": 43,
    "blueye.no": 1,
    "yahoo.com": 1,
    "myfastmail.com": 1,
    "agilent.com": 3,
    "dijkzeul.eu": 1,
    "snap.com": 1,
    "posteo.com": 12,
    "canogaperkins.net": 1,
    "eero.com": 1,
    "jahn....": 1,
    "tl-software.fi": 1,
    "sm...": 1,
    "loewe...": 1,
    "outlook.com": 1,
    "digi.com": 1,
    "desy.de": 1,
    "woodward.com": 1,
    "163.com": 1,
    "wyplay.com": 1,
    "port4949.net": 1
});

let baseUrl = 'http://47.120.41.97:8002/bugs/'

const fetchData = async () => {
    // try {
    //     const response = await axios.get(baseUrl + 'companies');
    //     data.value = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
    //     if (chart) {
    //         chart.setOption(getOption());
    //     }
    //     console.log(data)
    //     console.log(data.value)
    //     console.log(chart)
    //     console.log(chart.value)

    // } catch (error) {
    //     console.error('Error fetching data:', error);
    // }

    await axios.get(baseUrl + 'companies')
        .then(response => {
            console.log('responsedata', response.data);
            // 处理成功的情况
            data.value.data = response.data; // 假设后端返回的数据格式符合饼图需要的数据结构
            if (chart) {
                chart.setOption(getOption());
            }
            console.log('cdfufufuu', data.value.data)
        })
        .catch(error => {
            // 处理错误情况
            console.error('Error fetching data:', error);
        });

    if (chart) {
        chart.setOption(getOption());
        console.log('bbbb2', getOption().series[0].data)
    }
};

//initiate of pie chart
// const props = defineProps({
//     data: {
//         type: Array,
//         required: true
//     },
//     xAxisDataKey: {
//         type: String,
//         default: 'date'
//     },
//     yAxisDataKey: {
//         type: String,
//         default: 'value'
//     }
// });

const chartRef = ref(null);

let chart;

onMounted(() => {
    initChart();
});

// watch(
//     // () => props.data,
//     () => {
//         if (chart) {
//             chart.setOption(getOption());
//         }
//     },
//     { deep: true }
// );

const getOption = () => {
    console.log('a', Object.entries(data.value).map(([name, value]) => ({ name, value })))
    console.log('aa', data.value)
    return {
        title: {
            text: '企业数量统计',
            subtext: '按提交人邮箱后缀统计',
            // left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20
        },
        series: [
            {
                name: '占比',
                type: 'pie',
                radius: '80%',
                // data: Object.entries(data.value).map(item => ({
                //     value: item.value,
                //     name: item.name
                // })),
                // data: Object.entries(data.value).map(([name, value]) => ({ name, value })),
                data: Object.keys(data.value).map(name => ({
                    name,
                    value: data.value[name]
                })),
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
};

const initChart = () => {
    fetchData();
    console.log('aaaaaa', chartRef.value)
    chart = echarts.init(chartRef.value);
    chart.setOption(getOption());
    console.log('bbbb', getOption().series[0].data)
};

</script>