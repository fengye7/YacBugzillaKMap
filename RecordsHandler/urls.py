from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportedViewSet,ModifiedViewSet

router = DefaultRouter()
router.register('Reported', ReportedViewSet, basename='Reported')
router.register('Modified', ModifiedViewSet, basename='Modified')

urlpatterns = [
    path('', include(router.urls)),  # 将ViewSet中的URL路径添加到urlpatterns中
]