"""
URL configuration for YacBugzilla_KnowledgeMap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="YacBugzilla API平台",
        default_version="v2",
        description="接口文档",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='zcj2518529668@163.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('bugs/',include('DataHandler.urls')),
    path('records/',include('RecordsHandler.urls')),
    path('comments/',include(('CommentHandler.urls'))),
    path('rankings/',include(('RankingAnalysis.urls')))
]

