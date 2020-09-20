from django.contrib import admin

from .models import Tipo, Documento, Solicitud

admin.site.register(Tipo)
admin.site.register(Documento)
admin.site.register(Solicitud)
