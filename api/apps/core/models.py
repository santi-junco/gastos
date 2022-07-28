from django.db import models
from apps.usuario.models import Usuario

class TimeStampedModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name=u'creado', help_text=u'Fecha de creacion')
    modificado = models.DateTimeField(auto_now=True, verbose_name=u'modificado', help_text=u'Fecha de modificacion')

    class Meta:
        abstract = True

