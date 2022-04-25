import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .serializers import PrePopulatedUserSeriailzer, UserSerializer
from .models import CustomUser
from rest_framework.exceptions import NotFound
from rest_framework import status


User = get_user_model()


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})
        return Response(serializer.errors, status=400)


class LoginView(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            {'sub': user.id, 'exp': int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})


class CredentialsView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
      serializer = UserSerializer(request.user)
      return Response(serializer.data)


class GetUserById(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
      current_user = get_user_by_id(pk=pk)
      if current_user.id == request.user.id:
        serialized_user = PrePopulatedUserSeriailzer(current_user)
        return Response(data=serialized_user.data, status=status.HTTP_200_OK)


def get_user_by_id(pk):
  try:
    return CustomUser.objects.get(pk=pk)
  except CustomUser.DoesNotExist:
    raise NotFound(detail="Can't find that Coop Item")
    
