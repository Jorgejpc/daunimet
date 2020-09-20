from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('dcunimet/tipos', views.TipoListView)
router.register('dcunimet/documentos', views.DocumentoListView)
router.register('dcunimet/solicitudes', views.SolicitudListView)

urlpatterns = [
    path('', include(router.urls))
]
