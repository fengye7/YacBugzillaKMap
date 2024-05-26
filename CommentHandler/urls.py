from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentsViewSet

router = DefaultRouter()
router.register('Comments', CommentsViewSet, basename='Comments')

urlpatterns = [
    path('', include(router.urls)),  # 将ViewSet中的URL路径添加到urlpatterns中
]