import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AnalysisView from '../views/AnalysisView.vue';
import PredictionView from '../views/PredictionView.vue';
import KnowledgeMapView from '../views/KnowledgeMapView.vue';
import StatisticsView from '../views/StatisticsView.vue';
import ExhibitionView from '../views/ExhibitionView.vue'; // 数据展览

const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: AnalysisView,
  },
  {
    path: '/prediction',
    name: 'Prediction',
    component: PredictionView,
  },
  {
    path: '/knowledgeMap',
    name: 'KnowledgeMap',
    component: KnowledgeMapView,
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: StatisticsView,
  },
  {
    path: '/exhibition',
    name: 'Exhibition',
    component: ExhibitionView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
