from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import FeedSerializer
from .models import Feed


class Feeds(APIView):
    # api/v1/feeds
    # 전체 게시글 조회
    def get(self, request):
        feeds = Feed.objects.all()
        # 객체 -> json (serialize 필요)
        # ForeignKey로 User객체와 연결되어 있어 여러 객체를 사용: many = True 옵션 적용해야 함
        serialized = FeedSerializer(feeds, many = True)
        return Response(serialized.data)

    def post(self, request):
        # 역직렬화: 클라이언트가 보내준 json data -> object
        obj = FeedSerializer(data = request.data)
        # save전에 반드시 data validation 해줘야함
        if obj.is_valid():
            # 외래키 참조할 유저 객체도 같이 저장해야함(request.user -> 현재 로그인된 유저)
            feed = obj.save(author = request.user)

            # 방금 저장한 feed 객체를 화면 상에 보여주고 싶다: feed객체 -> json으로 직렬화 필요
            serialized = FeedSerializer(feed)
            print(serialized.data)
            return Response(serialized.data)
        else:
            return Response(obj.errors)

class FeedDetail(APIView):
    # api/v1/feeds/feed_id
    # 특정 게시글 객체 불러오기
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id = feed_id)
        except Feed.DoesNotExist: # 해당 피드가 없는 경우 Feed.DoesNotExist 라는 함수를 실행
            raise NotFound
    # 특정 게시글 조회
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        # object -> json : serialize
        serialized = FeedSerializer(feed)
        return Response(serialized.data)

