import datetime
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print("Email ", email, "\nPassword: ", password);
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        print("USER")
        print(user)
        payload = {
            'id': str(user.id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        print("PAYLOAD")
        print(payload)
        token = jwt.encode(payload, "secret", algorithm="HS256")
        print("TOKEN")
        print(token)
        response = Response({'jwt': token})
        print("RESPONSE DATA ", response.data);
        response.set_cookie(key='jwt', value=token, httponly=True)
        print("KUKIJI ", response.cookies);
        return response


class UserView(APIView):
    def get(self, request):
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

        return Response(serializer.data)
