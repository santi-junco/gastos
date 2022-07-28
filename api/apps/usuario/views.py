from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from .models import Usuario
from .serializers import *

# Creacion de usuario
class UsuarioCreateApiView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Listado de usuarios
# hacer que solamente el admin pueda ver la lista
class UsuarioListApiView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

# Editar usuario
class UsuarioUpdateApiView(UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Ver un usuario
class UsuarioVerApiView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Eliminar un usuario
# hacer eliminacion logica (is_active)
class UsuarioDeleteApiView(DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
