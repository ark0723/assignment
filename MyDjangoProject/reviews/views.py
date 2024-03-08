from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Review
from users.models import User
from feeds.models import Feed
from .serializer import ReviewSerializer

# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        # 여러개의 객체가 담겨있으므로 many=True를 추가해야함
        serialized = ReviewSerializer(reviews, many = True)
        return Response(serialized.data)

# api/v1/reviews/user_id [GET]
class ReviewByUser(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id = user_id)
        reviews = Review.objects.filter(user = user)
        serialized = ReviewSerializer(reviews, many = True)
        return Response(serialized.data)


# api/v1/reviews/feed_id [GET]
class ReviewByFeed(APIView):
    def get(self, request, feed_id):
        feed = Feed.objects.get(id = feed_id)
        reviews = Review.objects.filter(feed = feed)
        serialized = ReviewSerializer(reviews, many = True)
        return Response(serialized.data)


# api/v1/reviews/review_id [PUT, DELETE]
class ReviewDetail(APIView):
    def put(self, request, review_id):
        user = request.user
        reviews = Review.objects.filter(user = user)
        if review_id in [review.id for review in reviews]:
            review = Review.objects.get(id = review_id)
            update_review = ReviewSerializer(review, data = request.data, partial = True)
            if update_review.is_valid():
                updated = update_review.save()
                # updated review 객체 -> json으로 변경후 웹페이지에 띄움
                update_review = ReviewSerializer(updated)
                return Response(update_review.data)
            else:
                return Response(update_review.errors)

        else:
            raise ParseError("You are only allowed to edit reviews that you have written")

