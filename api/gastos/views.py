from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.usuario.models import Usuario

class ObtenerToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        usuario = Usuario.objects.get(emial=user)
        token = super().get_token(user)
        token['name'] = usuario.get_full_name()
        token['email'] = usuario.email
        return token

class Login(TokenObtainPairView):
    serializer_class = ObtenerToken