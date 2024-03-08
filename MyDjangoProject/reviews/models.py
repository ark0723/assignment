from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    content = models.CharField(max_length = 120)
    likes = models.PositiveIntegerField(default=0)
    # 누가 작성한 댓글인지(User:Review = 1: N)
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    # 어느 게시글(feed)에 달린 댓글인지(Feed: Review = 1: N)
    feed = models.ForeignKey('feeds.Feed', on_delete = models.CASCADE)


