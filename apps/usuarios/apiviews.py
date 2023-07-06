from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.db import transaction
from django.contrib.auth.hashers import make_password

from .models import Usuario
from .serializers import UserSerializer, RetrieveUserSerializer

from apps.core.functions import UserPermission

class CreateUserApiView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        with transaction.atomic():
            user = serializer.save()
            user.username = user.email
            user.password = make_password(self.request.data['password'])
            user.save()

class UpdateUserApiView(UserPermission, UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class RetrieveUserApiView(UserPermission, RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RetrieveUserSerializer

class DeleteUserApiView(UserPermission, DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
