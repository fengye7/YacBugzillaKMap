import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AnalysisView from "../views/AnalysisView.vue";
import PredictionView from "../views/PredictionView.vue";
import KnowledgeMapView from "../views/KnowledgeMapView.vue";
import StatisticsView from "../views/StatisticsView.vue";
import ExhibitionView from "../views/ExhibitionView.vue"; // 数据展览
import BugInfoView from "../views/BugInfoView.vue";
import LineChart from '../components/LineChart.vue';
import BarChart from '../components/BarChart.vue';
import BarChart2 from '../components/BarChart2.vue';
import PieChart from '../components/PieChart.vue';
import ScatterChart from '../components/ScatterChart.vue';

const routes = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/analysis",
    name: "analysis",
    component: AnalysisView,
  },
  {
    path: "/prediction",
    name: "prediction",
    component: PredictionView,
  },
  {
    path: "/knowledgeMap",
    name: "knowledgeMap",
    component: KnowledgeMapView,
  },
  {
    path: "/statistics",
    name: "statistics",
    component: StatisticsView,
    children: [
      {
        path: "line",
        name: "LineChart",
        component: LineChart,
      },
      {
        path: "bar",
        name: "BarChart",
        component: BarChart,
      },
      {
        path: "bar2",
        name: "BarChart2",
        component: BarChart2,
      },
      {
        path: "pie",
        name: "PieChart",
        component: PieChart,
      },
      {
        path: "scatter",
        name: "ScatterChart",
        component: ScatterChart,
      },
    ],
  },
  {
    path: "/exhibition/:type",
    name: "exhibition",
    component: ExhibitionView,
    props: true,
  },
  {
    path: "/bug/:id",
    name: "bug-info",
    component: BugInfoView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
