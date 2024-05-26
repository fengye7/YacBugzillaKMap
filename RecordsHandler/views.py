from rest_framework.viewsets import ModelViewSet

from RecordsHandler.models import Reported, Modified
from .serializers import ReportedSerializer, ModifiedSerializer


class ReportedViewSet(ModelViewSet):
    queryset = Reported.objects.all()
    serializer_class = ReportedSerializer
    search_fields = ('id')


class ModifiedViewSet(ModelViewSet):
    queryset = Modified.objects.all()
    serializer_class = ModifiedSerializer
    search_fields = ('id')
