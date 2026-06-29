from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken

from manager_app.serializers import RegisterSerializer
from manager_app.serializers.users import LoginSerializer
from manager_app.utils import (
    set_jwt_cookies,
    set_access_token,
    set_refresh_token,
    clear_cookies,
)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            username = request.data.get("username")
            user = User.objects.get(username=username)
            set_jwt_cookies(response, user)

        return response

    def get(self, request):
        return Response(
            {"detail": "Отправьте POST для входа."},
            status=status.HTTP_200_OK
        )


class CookieTokenRefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        refresh = request.COOKIES.get("refresh_token")

        if not refresh:
            return Response({"detail": "Refresh token отсутствует"}, status=400)

        try:
            token = RefreshToken(refresh)
        except InvalidToken:
            return Response({"detail": "Невалидный refresh token"}, status=401)

        access = token.access_token

        response = Response({"access": str(access)}, status=200)

        set_access_token(response, str(access))

        if token.get("exp"):
            set_refresh_token(response, str(token))

        return response

    def get(self, request):
        return Response(
            {"detail": "Используйте POST для обновления токена."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"detail": "Нажмите POST, чтобы выйти из аккаунта."},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        refresh = request.COOKIES.get("refresh_token")

        if refresh:
            try:
                token = RefreshToken(refresh)
                token.blacklist()
            except Exception:
                pass

        response = Response({"detail": "Вы вышли из аккаунта"})
        clear_cookies(response)
        return response
