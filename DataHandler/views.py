from collections import Counter
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
from RecordsHandler.serializers import ModifiedSerializer, ReportedSerializer

from django.db.models import Q,F

class BugsViewSet(ModelViewSet):
    queryset = BugTuple.objects.all()
    serializer_class = BugTupleSerializer
    search_fields = ('id')

    class LatestBugListView(APIView):
        @swagger_auto_schema(
            operation_description="获取最新的 10 个报告",
            responses={200: openapi.Response('最新报告的列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            bug_ids = list(Reported.objects.order_by('-time')[:10].values_list('bugId', flat=True))
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
                # 计算具有特定状态的记录数量
                count = BugTuple.objects.filter(status=bugstatus).count()
                # 直接返回计数作为响应内容
                return Response({"count": count}, status=status.HTTP_200_OK)
                # bugs = BugTuple.objects.filter(status=bugstatus).Count()
                # serializer = BugTupleSerializer(bugs, many=True)
                # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'status' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)
        
    class PriorityTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的优先级类型",
            responses={200: openapi.Response('优先级类型列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            p = BugTuple.objects.values_list('priority', flat=True).distinct()
            p_list = list(set(p))  # 保证唯一性
            return Response(p_list, status=status.HTTP_200_OK)

    class PriorityBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据优先级获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('priority', openapi.IN_QUERY, description="优先级", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            bugsp = request.query_params.get('priority')
            if bugsp:
                # 计算具有特定状态的记录数量
                count = BugTuple.objects.filter(priority=bugsp).count()
                # 直接返回计数作为响应内容
                return Response({"count": count}, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'priority' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

    class SeverityTypesView(APIView):
        @swagger_auto_schema(
            operation_description="获取唯一的严重性类型",
            responses={200: openapi.Response('严重性类型列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            s = BugTuple.objects.values_list('severity', flat=True).distinct()
            s_list = list(set(s))  # 保证唯一性
            return Response(s_list, status=status.HTTP_200_OK)

    class SeverityBugsView(APIView):
        @swagger_auto_schema(
            operation_description="根据严重性获取对应的 Bug 列表",
            manual_parameters=[
                openapi.Parameter('severity', openapi.IN_QUERY, description="严重性类型", type=openapi.TYPE_STRING)
            ],
            responses={200: openapi.Response('符合条件的 Bug 列表', BugTupleSerializer(many=True))}
        )
        def get(self, request):
            bugsev = request.query_params.get('severity')
            if bugsev:
                # 计算具有特定状态的记录数量
                count = BugTuple.objects.filter(severity=bugsev).count()
                # 直接返回计数作为响应内容
                return Response({"count": count}, status=status.HTTP_200_OK)
            return Response({"error": "缺少 'severity' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)
        
    class PriorityStatusCountView(APIView):
        @swagger_auto_schema(
            operation_description="根据优先级和状态获取对应的 Bug 列表的数量",
            manual_parameters=[
                openapi.Parameter('priority', openapi.IN_QUERY, description="优先级类型", type=openapi.TYPE_STRING),
                openapi.Parameter('status', openapi.IN_QUERY, description="状态类型", type=openapi.TYPE_STRING)
            ],
            responses={
                200: openapi.Response('符合条件的 Bug 数量', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'count': openapi.Schema(type=openapi.TYPE_INTEGER)})),
                400: '错误的请求参数'
            }
        )
        def get(self, request):
            p = request.query_params.get('priority')
            sta = request.query_params.get('status')

            if not p or not sta:
                # 如果缺少任何一个参数，则返回错误信息
                return Response({"error": "缺少 'priority' 或 'status' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

            # 使用Q对象进行多条件查询
            query = Q(status=sta) & Q(priority=p)
            count = BugTuple.objects.filter(query).count()

            # 直接返回计数作为响应内容
            return Response({"count": count}, status=status.HTTP_200_OK)

    class SeverityStatusCountView(APIView):
        @swagger_auto_schema(
            operation_description="根据严重性和状态获取对应的 Bug 列表的数量",
            manual_parameters=[
                openapi.Parameter('severity', openapi.IN_QUERY, description="严重性类型", type=openapi.TYPE_STRING),
                openapi.Parameter('status', openapi.IN_QUERY, description="状态类型", type=openapi.TYPE_STRING)
            ],
            responses={
                200: openapi.Response('符合条件的 Bug 数量', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'count': openapi.Schema(type=openapi.TYPE_INTEGER)})),
                400: '错误的请求参数'
            }
        )
        def get(self, request):
            severity = request.query_params.get('severity')
            sta = request.query_params.get('status')

            if not severity or not sta:
                # 如果缺少任何一个参数，则返回错误信息
                return Response({"error": "缺少 'severity' 或 'status' 查询参数"}, status=status.HTTP_400_BAD_REQUEST)

            # 使用Q对象进行多条件查询
            query = Q(status=sta) & Q(severity=severity)
            count = BugTuple.objects.filter(query).count()

            # 直接返回计数作为响应内容
            return Response({"count": count}, status=status.HTTP_200_OK)

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
            # companies = set()
            # for assignee in assignees:
            #     if '@' in assignee:
            #         domain = assignee.split('@')[-1]
            #         companies.add(domain)
            # return Response(list(companies), status=status.HTTP_200_OK)
            
            # 使用values_list获取assignee并去重
            assignees = BugTuple.objects.values_list('assignee', flat=True).distinct()
            
            # 初始化一个Counter对象来计数
            domain_counts = Counter()
            
            for assignee in assignees:
                if '@' in assignee:
                    domain = assignee.split('@')[-1]
                    domain_counts[domain] += 1
            
            # 构造目标格式的数据
            data = [{"value": count, "name": domain} for domain, count in domain_counts.items()]
            
            return Response({"data": data}, status=status.HTTP_200_OK)

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
        @swagger_auto_schema(
            operation_description="根据 Bug ID 获取对应的 Bug 详细信息",
            responses={200: openapi.Response('Bug ID 对应的 Bug 详细信息', BugTupleSerializer(many=True))}
        )
        def get(self, request, id):
            try:
                bug = BugTuple.objects.get(id=id)
            except BugTuple.DoesNotExist:
                return Response({"error": "Bug not found"}, status=status.HTTP_404_NOT_FOUND)

            comments = Comment.objects.filter(bugId=id)
            reported = Reported.objects.get(bugId=id)
            modifieds = Modified.objects.filter(bugId=id)

            bug_serializer = BugTupleSerializer(bug)
            comment_serializer = CommentSerializer(comments, many=True)
            reported_serializer = ReportedSerializer(reported)
            modified_serializer = ModifiedSerializer(modifieds, many=True)

            response_data = {
                'bug': bug_serializer.data,
                'comments': comment_serializer.data,
                'reported': reported_serializer.data,
                'modifieds': modified_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

    class KMapDataView(APIView):
        @swagger_auto_schema(
            operation_description="获取知识图谱信息",
            manual_parameters=[
                openapi.Parameter(
                    'domains', openapi.IN_QUERY,
                    description="竞争公司域名列表，用逗号分隔",
                    type=openapi.TYPE_STRING
                )
            ],
            responses={200: openapi.Response('返回数据库的知识图谱信息')}
        )
        def get(self, request):
            # 获取竞争公司域名列表
            domains_param = request.query_params.get('domains', 'intel.com')
            competitor_domains = [domain.strip() for domain in domains_param.split(',')]

            # 获取所有BugTuple记录
            bugs = BugTuple.objects.all()

            # 构建nodes和links数据结构
            nodes = []
            links = []
            node_set = set()  # 用于检查node是否已经存在
            link_set = set()  # 用于检查link是否已经存在

            for bug in bugs:
                # 过滤竞争公司
                if any(domain in bug.assignee for domain in competitor_domains) or \
                        any(any(domain in cc for cc in eval(bug.ccList)) for domain in competitor_domains):

                    # 创建产品和组件节点
                    product_node = {'id': f'product_{bug.product}', 'name': bug.product, 'category': 'product'}
                    component_node = {'id': f'component_{bug.component}', 'name': bug.component,
                                      'category': 'component'}
                    assignee_node = {'id': f'assignee_{bug.assignee}', 'name': bug.assignee, 'category': 'assignee'}

                    if product_node['id'] not in node_set:
                        nodes.append(product_node)
                        node_set.add(product_node['id'])

                    if component_node['id'] not in node_set:
                        nodes.append(component_node)
                        node_set.add(component_node['id'])

                    if assignee_node['id'] not in node_set:
                        nodes.append(assignee_node)
                        node_set.add(assignee_node['id'])

                    # 创建产品和组件之间的连接
                    product_component_link = {
                        'source': product_node['id'],
                        'target': component_node['id'],
                        'name': 'has_component'
                    }
                    if (product_component_link['source'], product_component_link['target']) not in link_set:
                        links.append(product_component_link)
                        link_set.add((product_component_link['source'], product_component_link['target']))

                    # 创建组件和指派人之间的连接
                    component_assignee_link = {
                        'source': component_node['id'],
                        'target': assignee_node['id'],
                        'name': 'assigned_to'
                    }
                    if (component_assignee_link['source'], component_assignee_link['target']) not in link_set:
                        links.append(component_assignee_link)
                        link_set.add((component_assignee_link['source'], component_assignee_link['target']))

            response_data = {
                'nodes': nodes,
                'links': links,
            }
            return Response(response_data, status=status.HTTP_200_OK)
