import datetime
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .serializers import AdminSerializer
from .permissions import AdminPermission


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.is_active = False
        serializer.save()
        return Response(serializer.data)


class RegisterAdminView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        print("treba da jeste superuser")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        print("USER")
        print(user)
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        print("PAYLOAD")
        print(payload)
        token = jwt.encode(payload, "secret", algorithm="HS256")
        print(token)
        response = Response({'jwt': token})
        print("RESPONSE DATA ", response.data);
        response.set_cookie(key='jwt', value=token, httponly=True, secure=True, samesite='None')
        print("KUKIJI ", response.cookies);
        return response


class UserView(APIView):
    def get(self, request):
        print("USER VIEW")
        print(request.COOKIES)
        token = request.COOKIES.get('jwt')
        print("TOKEN ", token);
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        print(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.set_cookie(key='jwt', httponly=True, secure=True, samesite='None')
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


# class UserViewSet(viewsets.ModelViewSet):
#     # permission_classes = (AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UsersViewSet(APIView):
    def get(self, request):
        queryset = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        response = Response(serializer.data, content_type="application/json")
        return response


class ChangeUserActivityView(APIView):
    def put(self, request):
        if not AdminPermission.has_permission(self, request):
            return Response({"detail": "You don't have admin permissions."}, status=403)

        data = json.loads(request.body.decode("utf-8"))
        email = data['email']
        print(email)
        user = User.objects.get(email=email)
        user.is_active = not user.is_active
        user.save()

        # token = request.COOKIES.get('jwt')
        # print("TOKEN ", token);
        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')
        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     raise AuthenticationFailed('Unauthenticated!')
        # user = User.objects.filter(id=payload['id']).first()
        # print("USER OD TOKENA JE ", user)
        #
        # if not AdminPermission.has_permission(self, user):
        #     return Response({"detail": "You don't have admin permissions."}, status=401)

        response = Response("successfuly changed user activity", content_type="application/json")
        return response
