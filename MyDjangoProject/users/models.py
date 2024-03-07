from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_business = models.BooleanField(default = False)
    grade = models.CharField(max_length = 5, default = "새싹") # 새싹, 잎새, 가지, 열매, 나무
    age = models.PositiveIntegerField(null = True, verbose_name = "나이")
    gender_choices = [('0', '여자'), 
                      ('1', '남자'), 
                      ('2', '트렌스젠더'), 
                      ('3', '논바이너리'), 
                      ('4', '밝히지 않음')] # (DB에 저장될 값, 사용자에게 표시할 값)
    gender = models.CharField(max_length = 10, default = 4, choices = gender_choices, verbose_name = "성별")
    # name = models.CharField(max_length = 20, verbose_name = "이름")
    # description = models.TextField(verbose_name = "프로필")
    # def __str__(self):
    #     return f'{self.name} / {self.age}세 / {self.gender}'