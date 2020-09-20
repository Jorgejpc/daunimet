from django.db import models
from datetime import timedelta
from django.utils import timezone


# Funciones
# Retorna 15 dias despues
def in_few_days():
    return timezone.now() + timedelta(days=15)

# Models
#################################################################################################################


class Tipo(models.Model):
    tipo = models.CharField(blank=False, unique=True, max_length=150,
                            verbose_name='Tipo documento:', help_text='Ingrese el tipo del documento')

    dias = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Numero de dias:', help_text='Ingrese el numero de dias')

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'


#################################################################################################################
class Documento(models.Model):
    nombre = models.CharField(blank=False, unique=False, max_length=150,
                              verbose_name='Nombre documento:', help_text='Ingrese el nombre del documento')

    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False, related_name='documento_tipo',
                                verbose_name='tipo documento:', help_text='Ingrese el tipo del documento')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'nombre'
        verbose_name_plural = 'nombres'


#################################################################################################################
class Solicitud(models.Model):
    correo = models.CharField(blank=False, unique=False, max_length=150,
                              verbose_name='Correo electronico:', help_text='Ingrese el correo electronico')

    id_documento = models.ForeignKey(Documento, on_delete=models.CASCADE, null=False, related_name='solicitud_documento',
                                     verbose_name='documento:', help_text='Ingrese el documento')

    fecha_solicitud = models.DateTimeField(auto_now=True)

    fecha_aprox = models.DateTimeField(default=in_few_days)

    fecha_listo = models.DateTimeField(null=True, blank=True)

    on_off = models.BooleanField(
        default=True, verbose_name='Solicitud Activa:', help_text='Inglese el estado de la solicitud')

    def __str__(self):
        return self.correo

    class Meta:
        ordering = ['correo']
        verbose_name = 'solicitud'
        verbose_name_plural = 'solicitudes'
