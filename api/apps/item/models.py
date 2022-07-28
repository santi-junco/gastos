from django.db import models
from apps.core.models import TimeStampedModel
from apps.usuario.models import Usuario

# Create your models here.
class Item(TimeStampedModel):
    fecha = models.DateField(null=False, blank=False)
    monto = models.FloatField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    activo = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

class GastoFijo(Item):

    def __str__(self) -> str:
        return self.id

class GastoDiario(Item):
    
    def __str__(self) -> str:
        return self.id

class Ingreso(Item):
    
    def __str__(self) -> str:
        return self.id