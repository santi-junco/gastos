from rest_framework import serializers

from .models import GastoFijo, GastoVariable, Ingreso

class GastoFijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastoFijo
        fields = '__all__'

class GastoVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastoVariable
        fields = '__all__'

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'
