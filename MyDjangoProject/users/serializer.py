from rest_framework.serializers import ModelSerializer
from .models import User

# 피드를 위한 유저 시리얼라이저: 민감한 개인정보를 숨기기 위해 생성함
class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'email','is_business', 'grade')

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"