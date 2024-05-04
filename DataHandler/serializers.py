from rest_framework import serializers

from DataHandler.models import BugTuple


class BugTupleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugTuple
        fields = "__all__"
