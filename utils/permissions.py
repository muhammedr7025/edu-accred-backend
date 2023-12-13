from rest_framework import authentication
import jwt
from django.conf import settings
from rest_framework.response import Response

class JWTUtils:
    @staticmethod
    def fetch_role(request):
        token = authentication.get_authorization_header(request).decode("utf-8").split()
        payload = jwt.decode(
            token[1], settings.SECRET_KEY, algorithms=["HS256"], verify=True
        )
        role = payload.get("role")
        if role is None:
            raise Exception(
                "The corresponding JWT token does not contain the 'role' key"
            )
        return role


def role_required(roles):
    def decorator(view_func):
        def wrapped_view_func(obj, request, *args, **kwargs):
            role =  JWTUtils.fetch_role(request)
            print(role)
            if role in roles:
                response = view_func(obj, request, *args, **kwargs)
                return response
            res = Response({
                "status":"error",
                "message":"You do not have the required role to access this page."}
            )
            return res

        return wrapped_view_func

    return decorator