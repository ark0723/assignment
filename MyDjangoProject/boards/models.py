from django.db import models
from common.models import CommonModel

# 게시글:  title, content, writer, date, likes, reviews
class Board(CommonModel):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    writer = models.CharField(max_length = 30, default = 'mobbom')
    date = models.DateTimeField(auto_now_add = True)
    likes = models.PositiveIntegerField(default = 0)
    reviews = models.PositiveIntegerField(default = 0)
    # n_delete = models.CASCADE - 유저가 삭제되면 foreignKey로 연결된 해당 포스트도 삭제
    # user = models.ForeignKey("users.User", related_name = "user",db_column = "id",on_delete = models.CASCADE)
    user = models.ForeignKey("users.User",on_delete = models.CASCADE)
    # def __str__(self):
    #     return self.title

