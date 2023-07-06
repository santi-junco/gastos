from django.db import models

from apps.core.models import TimeStampedModel
from apps.usuarios.models import Usuario

PRIORIDAD_CHOICES = (
    ("Baja","Baja"),
    ("Media","Media"),
    ("Alta","Alta")
)

class Movimiento(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.TextField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        abstract = True

class GastoFijo(Movimiento):
    fecha_vencimiento = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Baja')
    pagado = models.BooleanField(default=False)


class GastoVariable(Movimiento):
    pass

class Ingreso(Movimiento):
    pass