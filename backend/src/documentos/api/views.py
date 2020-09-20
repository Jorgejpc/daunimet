from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from django.shortcuts import render

from documentos.models import Tipo
from .serializers import TipoSerializer

from documentos.models import Documento
from .serializers import DocumentoSerializer

from documentos.models import Solicitud
from .serializers import SolicitudSerializer

#################################################################################################################


class TipoListView(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


#################################################################################################################


class DocumentoListView(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


#################################################################################################################


class SolicitudListView(viewsets.ModelViewSet):
    queryset = Solicitud.objects.filter(on_off=True)
    serializer_class = SolicitudSerializer


#################################################################################################################
