from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', views.Users.as_view()),
    path('myinfo/', views.MyInfo.as_view()),
    # authentication
    path('getToken', obtain_auth_token), #username, password를 보내면 토큰을 반환
    path("login",views.Login.as_view()), # Django Session Login
    path("logout", views.Logout.as_view()), # logout

    #JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailVeiw.as_view()),

    # simple JWT authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMDgxNzk4NSwiaWF0IjoxNzEwMjEzMTg1LCJqdGkiOiJlZWJiNGEwMDdlZTU0MzBkYTIzNTQ4YmQ4NjRlMzhkOCIsInVzZXJfaWQiOjR9.145vMh639sKiC81XQuF-PnqdyhDcbTbzFwn_jWl3rWo",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjE2Nzg1LCJpYXQiOjE3MTAyMTMxODUsImp0aSI6IjczNmFhMDBkZmE3OTQzNWJhNDkzNDM4ZmIwM2ZkMzNjIiwidXNlcl9pZCI6NH0.7Dficb_UI7YnFxJ800ZQ-wNa8DQvfdYHRuSvfuU_GJQ"
# }