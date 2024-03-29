from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tadmin.views import UserInfoViewSet

# router = DefaultRouter() // 这个是Django的api格式；下面是swagger的api格式
# router = routers.DefaultRouter()
# router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API平台",
        default_version="v1",
        description="接口文档",
        terms_of_service="",
        contact=openapi.Contact(email='2152814@tongji.edu.cn'),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
]

urlpatterns += [
    path('', include(router.urls)),
]
urlpatterns += [
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
]
