from django.db import models
from common.models import CommonModel


class Feed(CommonModel):
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length = 120)
    # author: feed  = 1: N
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)


