import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AnalysisView from '../views/AnalysisView.vue';
import PredictionView from '../views/PredictionView.vue';
import KnowledgeMapView from '../views/KnowledgeMapView.vue';
import StatisticsView from '../views/StatisticsView.vue';
import ExhibitionView from '../views/ExhibitionView.vue'; // 数据展览
import BugInfoView from '../views/BugInfoView.vue'

const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/analysis',
    name: 'analysis',
    component: AnalysisView,
  },
  {
    path: '/prediction',
    name: 'prediction',
    component: PredictionView,
  },
  {
    path: '/knowledgeMap',
    name: 'knowledgeMap',
    component: KnowledgeMapView,
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: StatisticsView,
  },
  {
    path: '/exhibition/:type',
    name: 'exhibition',
    component: ExhibitionView,
    props: true,
  },
  {
    path: '/bug/:id',
    name: 'bug-info',
    component: BugInfoView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
