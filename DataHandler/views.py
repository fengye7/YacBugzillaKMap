from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DataHandler.models import BugTuple
from RecordsHandler.models import Reported
from .serializers import BugTupleSerializer

class BugsViewSet(ModelViewSet):
    queryset = BugTuple.objects.all()
    serializer_class = BugTupleSerializer
    search_fields = ('id')
    
    class LatestBugListView(APIView):
        def get(self, request):
            # 获取最新的 100 个报告的 ID
            bug_ids = list(Reported.objects.order_by('-time')[:100].values_list('bugId', flat=True))

            print(bug_ids)
        
            # 获取这些 ID 对应的 BugTuple 记录
            bug_tuples = BugTuple.objects.filter(id__in=bug_ids)

            # 序列化数据
            serializer = BugTupleSerializer(bug_tuples, many=True)

            # 返回 JSON 格式的响应
            return Response(serializer.data, status=status.HTTP_200_OK)

