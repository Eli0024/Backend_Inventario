from django.urls import path
from . import views 
from .views import (RegistrarEquipoView, RegistrarUsuarioView, RegistrarLicenciaView, RegistrarMapaView, MantenimientoView,
DocumentoView, RegistrarEquipoDetailView, RegistrarUsuarioDetailView, RegistrarLicenciaDetailView, RegistrarMapaDetailView,
DocumentoDetailView, MantenimientoDetailView)

urlpatterns = [
    path('registrarequipo/', RegistrarEquipoView.as_view(), name="listaequipo"),
    path('registrarequipo/<int:pk>/', RegistrarEquipoDetailView.as_view(), name="registrarequipo"),
    path('usuarios/', RegistrarUsuarioView.as_view(), name='listausuarios'),
    path('registrarusuario/<int:pk>/', RegistrarUsuarioDetailView.as_view(), name="registrarusuario"),
    path('licencias/', RegistrarLicenciaView.as_view(), name='listalicencia'),
    path('licencias/<int:pk>/', RegistrarLicenciaDetailView.as_view(), name='licencias'),
    path('mantenimiento/', MantenimientoView.as_view(), name='listamantenimiento'),
    path('mantenimiento/<int:pk>/', MantenimientoDetailView.as_view(), name='mantenimiento'),
    path('documento/', DocumentoView.as_view(), name='listadocumento'),
    path('documento/<int:pk>/', DocumentoDetailView.as_view(), name='documento')
]