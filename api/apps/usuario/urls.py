from django.urls import path
from .views import *

urlpatterns = [
    path('crear/', UsuarioCreateApiView.as_view()),
    path('listar/', UsuarioListApiView.as_view()),
    path('ver/<int:pk>/', UsuarioVerApiView.as_view()),
    path('editar/<int:pk>/', UsuarioUpdateApiView.as_view()),
    path('eliminar/<int:pk>/', UsuarioDeleteApiView.as_view()),
]
