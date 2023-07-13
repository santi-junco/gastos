from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.db import transaction

from apps.usuarios.models import Usuario
from apps.core.exceptions import CustomException

class ObteainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        with transaction.atomic():
            # tiene un campo user_id por defaul 
            token = super().get_token(user)
            # token['user'] = {
            #     'email': user.email,
            # }
            return token
        
class ObtainToken(TokenObtainPairView):
    def get_serializer_class(self):
        try:
            Usuario.objects.get(email=self.request.data['email'])
        except:
            raise CustomException("Usuario no encontrado")
        
        return ObteainTokenSerializer

class TestApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        content = {
            'mensaje': 'Bienvenido/a a Gastos. API Funcionando ok!'
        }
        return Response(content)
