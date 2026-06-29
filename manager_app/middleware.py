import time
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
from .utils import set_access_token, clear_cookies


class SimpleJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access = request.COOKIES.get("access_token")
        refresh = request.COOKIES.get("refresh_token")

        new_access = None
        clear = False

        if access or refresh:

            if access and self._is_access_valid(access):
                request.META["HTTP_AUTHORIZATION"] = f"Bearer {access}"

            elif refresh and self._is_refresh_valid(refresh):
                new_access = self._mint_access(refresh)
                if new_access:
                    request.META["HTTP_AUTHORIZATION"] = f"Bearer {new_access}"
                else:
                    clear = True

            else:
                clear = True

        response = self.get_response(request)

        if clear:
            clear_cookies(response)
        elif new_access:
            set_access_token(response, new_access)

        return response

    def _is_access_valid(self, token_str):
        try:
            token = AccessToken(token_str)
            return int(token["exp"]) > int(time.time())
        except Exception:
            return False

    def _is_refresh_valid(self, token_str):
        try:
            RefreshToken(token_str)
            return True
        except Exception:
            return False

    def _mint_access(self, refresh_str):
        try:
            refresh = RefreshToken(refresh_str)
            return str(refresh.access_token)
        except Exception:
            return None
