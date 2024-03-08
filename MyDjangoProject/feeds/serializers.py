from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializer import FeedUserSerializer
from reviews.serializer import ReviewSerializer

class FeedSerializer(ModelSerializer):
    # author: feed = 1 : N
    author = FeedUserSerializer(read_only = True)
    # review: feed = N: 1 -> reverse processor 필요,
    # read_only= True(feed 변경시, 댓글은 변경 되어서는 안됨)
    # 여러 개의 댓글: many = True
    review_set = ReviewSerializer(read_only = True, many = True)
    class Meta:
        model = Feed # 어떤 모델을 직렬화 할거냐 지정
        fields = '__all__' # 전체 필드 직렬화
        # default: depth = 0 -> 외래키로 참조되는 user 객체의 아이디만 보여줌
        # deapth = 1 ->외래키로 참조되는 user 객체의 디테일을 모두 보여줌
        depth = 1