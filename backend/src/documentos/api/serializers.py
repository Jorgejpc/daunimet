from rest_framework import serializers
from documentos.models import Tipo
from documentos.models import Documento
from documentos.models import Solicitud


#################################################################################################################


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'tipo', 'dias')


#################################################################################################################


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('id', 'nombre', 'id_tipo')


#################################################################################################################


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'correo', 'id_documento', 'fecha_solicitud', 'fecha_aprox',
                  'fecha_listo', 'on_off')


#################################################################################################################
