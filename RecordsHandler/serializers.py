from rest_framework import serializers

from RecordsHandler.models import Reported, Modified


class ReportedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reported
        fields = "__all__"


class ModifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modified
        fields = "__all__"
