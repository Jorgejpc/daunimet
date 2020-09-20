from django.contrib import admin
from .models import Tipo, Documento, Solicitud

#########################################################################
class TipoAdmin(admin.ModelAdmin):

    list_display = ('id','tipo', 'dias')
    #list_filter = ('tipo',)
    search_fields = ('tipo',)
    ordering = ('id',)

admin.site.register(Tipo, TipoAdmin)

#########################################################################
class DocumentoAdmin(admin.ModelAdmin):

    list_display = ('id','nombre', 'id_tipo')
    list_filter = ('id_tipo',)
    search_fields = ('nombre',)
    ordering = ('id',)

admin.site.register(Documento, DocumentoAdmin)

#########################################################################
class SolicitudAdmin(admin.ModelAdmin):

    list_display = ('id','correo', 'id_documento', 'fecha_solicitud', 'fecha_aprox', 'fecha_listo', 'on_off')
    list_filter = ('id_documento',)
    search_fields = ('correo',)
    ordering = ('id',)

admin.site.register(Solicitud, SolicitudAdmin)