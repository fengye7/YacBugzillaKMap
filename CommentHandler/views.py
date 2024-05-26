from rest_framework.viewsets import ModelViewSet

from CommentHandler.models import Comment
from .serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ('id')