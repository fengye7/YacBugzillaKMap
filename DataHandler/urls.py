from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BugsViewSet

router = DefaultRouter()
router.register('BugTuples', BugsViewSet, basename='BugTuples')

urlpatterns = [
    path('latest-bugs/', BugsViewSet.LatestBugListView.as_view(), name='latest_bugs'),
    path('all-bugs/', BugsViewSet.AllBugListView.as_view(), name='all_bugs'),
    path('product-components/', BugsViewSet.ProductComponentTypesView.as_view(), name='product_component_types'),
    path('product-component-bugs/', BugsViewSet.ProductComponentBugsView.as_view(), name='product_component_bugs'),
    path('statuses/', BugsViewSet.StatusTypesView.as_view(), name='status_types'),
    path('status-bugs/', BugsViewSet.StatusBugsView.as_view(), name='status_bugs'),
    path('status-bugs-list/', BugsViewSet.StatusBugListView.as_view(), name='status_bugs_list'),
    path('platforms/', BugsViewSet.PlatformTypesView.as_view(), name='platform_types'),
    path('platform-bugs/', BugsViewSet.PlatformBugsView.as_view(), name='platform_bugs'),
    path('companies/', BugsViewSet.CompanyTypesView.as_view(), name='company_types'),
    path('company-bugs/', BugsViewSet.CompanyBugsView.as_view(), name='company_bugs'),
    path('bug-info/<int:id>/', BugsViewSet.BugInfoView.as_view(), name='bug_info'),
    path('k-map-data/', BugsViewSet.KMapDataView.as_view(), name='k_map_data'),
    path('priority/', BugsViewSet.PriorityTypesView.as_view(), name='priority'),
    path('priorityCount/', BugsViewSet.PriorityBugsView.as_view(), name='priorityCount'),
    path('severity/', BugsViewSet.SeverityTypesView.as_view(), name='severity'),
    path('severityCount/', BugsViewSet.SeverityBugsView.as_view(), name='severityCount'),
    path('priorityStatusCount/', BugsViewSet.PriorityStatusCountView.as_view(), name='PriorityStatusCount'),
    path('severityStatusCount/', BugsViewSet.SeverityStatusCountView.as_view(), name='SeverityStatusCount'),
    path('', include(router.urls)),  # 将BugsViewSet中的URL路径添加到urlpatterns中
]
