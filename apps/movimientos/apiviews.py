from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView

from django.db import transaction
from django.http.response import JsonResponse

from .models import GastoFijo, GastoVariable, Ingreso
from .serializers import GastoFijoSerializer, GastoVariableSerializer, IngresoSerializer

from apps.core.functions import get_token

#### Ingresos
class IngresoCreateApiView(CreateAPIView):
    serializer_class = IngresoSerializer

class IngresoListApiView(ListAPIView):
    serializer_class = IngresoSerializer
    def get_queryset(self):
        token = get_token(self.request)
        queryset = Ingreso.objects.filter(usuario=token['user_id'])
        return queryset

class IngresoUpdateApiView(UpdateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

    def perform_update(self, serializer):
        with transaction.atomic():
            token = get_token(self.request)
            ingreso = serializer.save()
            
            if token['user_id'] != ingreso.usuario:
                return JsonResponse({'detail': 'No se encontro el ingreso especificado'}, status=404)
        
        return super().perform_update(serializer)

class IngresoDeleteApiView(DestroyAPIView):
    serializer_class = IngresoSerializer
    queryset = Ingreso.objects.all()

    def perform_destroy(self, instance):
        with transaction.atomic():
            token = get_token(self.request)
            if token['user_id'] != instance.id:
                return JsonResponse({'detail': 'No se encontro el ingreso a eliminar'}, status=404)

            return super().perform_destroy(instance)

#######################################################
#### Gasto Fijo

class GastoFijoCreateApiView(CreateAPIView):
    serializer_class = GastoFijoSerializer

class GastoFijoListApiView(ListAPIView):
    serializer_class = GastoFijoSerializer
    
    def get_queryset(self):
        token = get_token(self.request)
        queryset = GastoFijo.objects.filter(usuario=token['user_id'])
        return queryset

class GastoFijoUpdateApiView(UpdateAPIView):
    serializer_class = GastoFijoSerializer
    
    def perform_update(self, serializer):
        with transaction.atomic():
            token = get_token(self.request)
            gato_fijo = serializer.save()
            
            if token['user_id'] != gato_fijo.usuario:
                return JsonResponse({'detail': 'No se encontro el gasto fijo especificado'}, status=404)
            
            # talves tenga que pasarle gasto_fijo en ves de serializer
            return super().perform_update(serializer)

class GastoFijoDeleteApiView(DestroyAPIView):
    serializer_class = GastoFijoSerializer
    
    def perform_destroy(self, instance):
        with transaction.atomic():
            token = get_token(self.request)
            if token['user_id'] != instance.usuario:
                return JsonResponse({'detail': 'No se encontro el gasto fijo especificado'}, status=404)
            
            return super().perform_destroy(instance)

####################################################
#### Gatos Variable
class GastoVariableCreateApiView(CreateAPIView):
    serializer_class = GastoVariableSerializer

class GastoVariableListApiView(ListAPIView):
    serializer_class = GastoVariableSerializer
    
    def get_queryset(self):
        token = get_token(self.request)
        queryset = GastoVariable.objects.filter(usuario=token['user_id'])
        return queryset

class GastoVariableUpdateApiView(UpdateAPIView):
    serializer_class = GastoVariableSerializer
    
    def perform_update(self, serializer):
        with transaction.atomic():
            token = get_token(self.request)
            gato_variable = serializer.save()
            
            if token['user_id'] != gato_variable.usuario:
                return JsonResponse({'detail': 'No se encontro el gasto variable especificado'}, status=404)
            
            # talves tenga que pasarle gasto_variable en ves de serializer
            return super().perform_update(serializer)

class GastoVariableDeleteApiView(DestroyAPIView):
    serializer_class = GastoVariableSerializer
    
    def perform_destroy(self, instance):
        with transaction.atomic():
            token = get_token(self.request)
            if token['user_id'] != instance.usuario:
                return JsonResponse({'detail': 'No se encontro el gasto variable especificado'}, status=404)
            
            return super().perform_destroy(instance)