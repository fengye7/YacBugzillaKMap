from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from DataHandler.models import BugTuple
from .serializers import BugTupleSerializer
from CommentHandler.models import Comment
from CommentHandler.serializers import CommentSerializer
from RecordsHandler.models import Reported, Modified
from RecordsHandler.serializers import ModifiedSerializer


class BugsViewSet(ModelViewSet):
    queryset = BugTuple.objects.all()
    serializer_class = BugTupleSerializer
    search_fields = ('id')

    class LatestBugListView(APIView):
        @swagger_auto_schema(
            operation_description="获取最新的 100 个报告",
            responses={200: openapi.Response('最新报告的列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            bug_ids = list(Reported.objects.order_by('-time')[:100].values_list('bugId', flat=True))
            bug_tuples = BugTuple.objects.filter(id__in=bug_ids)
            serializer = BugTupleSerializer(bug_tuples, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    class ProductComponentTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的产品和组件组合",
            responses={200: openapi.Response('产品和组件组合列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            product_components = BugTuple.objects.values('product', 'component').distinct()
            product_component_list = list(product_components)
            unique_product_components = {(item['product'], item['component']) for item in product_component_list}
            unique_product_component_list = [{'product': pc[0], 'component': pc[1]} for pc in unique_product_components]
            return Response(unique_product_component_list, status=status.HTTP_200_OK)

    class ProductComponentBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据产品和组件获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('product', openapi.IN_QUERY, description="产品名称", type=openapi.TYPE_STRING),
                openapi.Parameter('component', openapi.IN_QUERY, description="组件名称", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            product = request.query_params.get('product')
            component = request.query_params.get('component')
            if product and component:
                bugs = BugTuple.objects.filter(product=product, component=component)
                serializer = BugTupleSerializer(bugs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'product' 或 'component' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

    class StatusTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的状态类型",
            responses={200: openapi.Response('状态类型列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            statuses = BugTuple.objects.values_list('status', flat=True).distinct()
            status_list = list(set(statuses))  # 保证唯一性
            return Response(status_list, status=status.HTTP_200_OK)

    class StatusBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据状态获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('status', openapi.IN_QUERY, description="状态类型", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            bugstatus = request.query_params.get('status')
            if bugstatus:
                bugs = BugTuple.objects.filter(status=bugstatus)
                serializer = BugTupleSerializer(bugs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'status' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

    class PlatformTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的平台类型",
            responses={200: openapi.Response('平台类型列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            platforms = BugTuple.objects.values_list('platform', flat=True).distinct()
            platform_list = list(set(platforms))  # 保证唯一性
            return Response(platform_list, status=status.HTTP_200_OK)

    class PlatformBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据平台获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('platform', openapi.IN_QUERY, description="平台类型", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            platform = request.query_params.get('platform')
            if platform:
                bugs = BugTuple.objects.filter(platform=platform)
                serializer = BugTupleSerializer(bugs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'platform' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

    class CompanyTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的公司类型",
            responses={200: openapi.Response('公司类型列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            assignees = BugTuple.objects.values_list('assignee', flat=True).distinct()
            companies = set()
            for assignee in assignees:
                if '@' in assignee:
                    domain = assignee.split('@')[-1]
                    companies.add(domain)
            return Response(list(companies), status=status.HTTP_200_OK)

    class CompanyBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据公司获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('company', openapi.IN_QUERY, description="公司名称", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            company = request.query_params.get('company')
            if company:
                bugs = BugTuple.objects.filter(assignee__endswith=f'@{company}')
                serializer = BugTupleSerializer(bugs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'company' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

    class BugInfoView(APIView):
        def get(self, request, id):
            try:
                bug = BugTuple.objects.get(id=id)
            except BugTuple.DoesNotExist:
                return Response({"error": "Bug not found"}, status=status.HTTP_404_NOT_FOUND)

            comments = Comment.objects.filter(bugId=id)
            modifieds = Modified.objects.filter(bugId=id)

            bug_serializer = BugTupleSerializer(bug)
            comment_serializer = CommentSerializer(comments, many=True)
            modified_serializer = ModifiedSerializer(modifieds, many=True)

            response_data = {
                'bug': bug_serializer.data,
                'comments': comment_serializer.data,
                'modifieds': modified_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)