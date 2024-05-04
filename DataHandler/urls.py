from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BugsViewSet

router = DefaultRouter()
router.register('BugTuples', BugsViewSet, basename='BugTuples')

urlpatterns = [
    path('latest-bugs/', BugsViewSet.LatestBugListView.as_view(), name='latest_bugs'),  # 将LatestBugListView视图的URL路径添加到urlpatterns中
    path('', include(router.urls)),  # 将BugsViewSet中的URL路径添加到urlpatterns中
]
