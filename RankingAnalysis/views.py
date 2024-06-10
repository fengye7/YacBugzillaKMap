# from .serializers import ReportedSerializer, ModifiedSerializer, BugTupleSerializer
from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from CommentHandler.models import Comment
from DataHandler.models import BugTuple
from RecordsHandler.models import Modified, Reported


class LatestReportedProductsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n个bug的product热度排行",
    )
    def get(self, request, n, format=None):
        latest_reported_ids = list(Reported.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        product_counts = BugTuple.objects.filter(id__in=latest_reported_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class LatestReportedComponentsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n个bug的component热度排行",
    )
    def get(self, request, n, format=None):
        latest_reported_ids = list(Reported.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        component_counts = BugTuple.objects.filter(id__in=latest_reported_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)


class LatestModifiedProductsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n次bug修改的product热度排行",
    )
    def get(self, request, n, format=None):
        latest_modified_ids = list(Modified.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        product_counts = BugTuple.objects.filter(id__in=latest_modified_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class LatestModifiedComponentsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n次bug修改的component热度排行",
    )
    def get(self, request, n, format=None):
        latest_modified_ids = list(Modified.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        component_counts = BugTuple.objects.filter(id__in=latest_modified_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)


class LatestCommentedProductsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n个评论所在bug的product的热度排行",
    )
    def get(self, request, n, format=None):
        latest_modified_ids = list(Comment.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        product_counts = BugTuple.objects.filter(id__in=latest_modified_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class LatestCommentedComponentsView(APIView):
    @swagger_auto_schema(
        operation_description="获取近n个评论所在bug的component的热度排行",
    )
    def get(self, request, n, format=None):
        latest_modified_ids = list(Comment.objects.order_by(
            '-time').values_list('bugId', flat=True)[:n])
        component_counts = BugTuple.objects.filter(id__in=latest_modified_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)


class ReportedProductsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的bug的product热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_reported = Reported.objects.filter(time__gte=cutoff_date)
        bug_ids = latest_reported.values_list('bugId', flat=True)
        product_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class ReportedComponentsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的bug的component热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_reported = Reported.objects.filter(time__gte=cutoff_date)
        bug_ids = latest_reported.values_list('bugId', flat=True)
        component_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)


class ModifiedProductsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的bug修改的component热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_modified = Modified.objects.filter(time__gte=cutoff_date)
        bug_ids = latest_modified.values_list('bugId', flat=True)
        product_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class ModifiedComponentsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的bug修改的component热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_modified = Modified.objects.filter(time__gte=cutoff_date)
        bug_ids = latest_modified.values_list('bugId', flat=True)
        component_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)


class CommentedProductsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的评论所在bug的component热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_commented = Comment.objects.filter(
            time__gte=cutoff_date)  # 假设有一个 Commented 模型
        bug_ids = latest_commented.values_list('bugId', flat=True)
        product_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'product').annotate(count=Count('product')).order_by('-count')
        return Response(product_counts, status=status.HTTP_200_OK)


class CommentedComponentsByDaysView(APIView):
    @swagger_auto_schema(
        operation_description="获取近days天的评论所在bug的component热度排行",
    )
    def get(self, request, days, format=None):
        cutoff_date = timezone.now() - timezone.timedelta(days=days)
        latest_commented = Comment.objects.filter(
            time__gte=cutoff_date)  # 假设有一个 Commented 模型
        bug_ids = latest_commented.values_list('bugId', flat=True)
        component_counts = BugTuple.objects.filter(id__in=bug_ids).values(
            'component').annotate(count=Count('component')).order_by('-count')
        return Response(component_counts, status=status.HTTP_200_OK)
