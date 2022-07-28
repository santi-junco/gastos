from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        models = Usuario
        fields = ['id', 'userName', 'email']