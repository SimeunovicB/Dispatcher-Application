from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
import jwt
from .models import User

# class AdminPermission(permissions.BasePermission):
#
#     def has_permission(self, user):
#         print("has_permission")
#         return user.is_superuser


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request):
        print("has_permission")
        token = request.COOKIES.get('jwt')
        print("TOKEN ", token);
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        print("USER OD TOKENA JE ", user)

        return user.is_superuser


class UserPermission(permissions.BasePermission):

    def has_permission(self, request):
        print("has_permission")
        token = request.COOKIES.get('jwt')
        print("TOKEN ", token);
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        return True