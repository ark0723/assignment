from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializer import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# 로그인한 해당 사용자만 user페이지를 볼 수 있도록 authentication 설정
from rest_framework.authentication import TokenAuthentication # 토큰 이용한 사용자 인증
from rest_framework.permissions import IsAuthenticated # 권한부여


class Users(APIView):
    def post(self, request):
        # api/v1/users/ : ['POST'] -> 유저생성

        # password -> 1. 검증 2. hash 필요
        password = request.data.get("password")
        # data= : 빼먹으면 안됨 -> 빼먹으면 오류 발생
        new_info = MyInfoUserSerializer(data = request.data) # json -> 객체

        # validate password
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")

        if new_info.is_valid(): # 객체 myinfo가 유효한지 체크해야함
            new_user = new_info.save() # 새로운 유저 생성
            new_user.set_password(password) # set_password(): 비밀번호 해쉬화
            new_user.save()
            # 웹페이지상에 생성된 객체 -> json화 하여 보여주기
            serialized = MyInfoUserSerializer(new_user)
            return Response(serialized.data)

        else:
            raise ParseError(new_info.errors)


class MyInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # api/v1/users/myinfo [GET, PUT]
    def get(self, request):
        user = request.user # 현재 로그인된 user를 받아옴
        current_user = MyInfoUserSerializer(user) # json -> 객체
        return Response(current_user.data)

    def put(self, request):
        user = request.user
        # partial = True -> 전체 객체를 업데이트 하는 대신 전달된 데이터의 일부만 사용하여 필드를 부분적으로 업데이트
        current_user = MyInfoUserSerializer(user,
                                            data = request.data,
                                            partial = True)

        if current_user.is_valid():
            updated_user = current_user.save()
            # updated_user 객체 -> json으로 변경후 웹페이지에 띄움
            current_user = MyInfoUserSerializer(updated_user)
            return Response(current_user.data)
        else:
            return Response(current_user.errors)



