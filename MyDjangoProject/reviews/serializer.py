from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializer import MyInfoUserSerializer, FeedUserSerializer


class ReviewSerializer(ModelSerializer):
    # Serializer(read_only = True) : API 결과에 포함되지만, 등록(create), 수정(update)시에 요청 파라미터에는 포함되지 않음
    # default값은 False이며, request 파라미터에 포함시키지 않으려면 True로 설정할것
    user = FeedUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'