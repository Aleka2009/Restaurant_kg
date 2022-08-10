from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from custom_auth.models import MyUser
from custom_auth.serializers import UserSerializer, LoginSerializer


class UserRegisterAPIViews(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})

        # if serializer.is_valid():
        #     serializer.save()
        #     return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        # return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""ПРОВЕРКА ЛОГИНА И ПАРОЛЯ. ВРУЧНУЮ"""


class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        login = request.data.get('email')
        if not MyUser.objects.filter(email=login).exists():
            return Response(
                f'{login} - does not exists'
            )
        user = MyUser.objects.get(email=login)
        password = request.data.get('password')
        pass_check = user.check_password(password)
        if not pass_check:
            return Response({'email or password incorrect'})
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})
