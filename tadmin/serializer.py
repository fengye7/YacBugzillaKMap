from tadmin.models import UserInfo
from rest_framework import serializers

# 序列化
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
