from django.urls import path
from . import views 
from .views import (RegistrarEquipoView, RegistrarUsuarioView, RegistrarLicenciaView, RegistrarMapaView, MantenimientoView,
RegistrarImpresoraView, RegistrarEquipoDetailView, RegistrarUsuarioDetailView, RegistrarLicenciaDetailView, RegistrarMapaDetailView,
RegistrarImpresoraDetailView, MantenimientoDetailView)

urlpatterns = [
    path('registrarequipo/', RegistrarEquipoView.as_view(), name="listaequipo"),
    path('registrarequipo/<int:pk>/', RegistrarEquipoDetailView.as_view(), name="registrarequipo"),
    path('usuarios/', RegistrarUsuarioView.as_view(), name='listausuarios'),
    path('usuarios/<int:pk>/', RegistrarUsuarioDetailView.as_view(), name="registrarusuario"),
    path('licencias/', RegistrarLicenciaView.as_view(), name='listalicencia'),
    path('licencias/<int:pk>/', RegistrarLicenciaDetailView.as_view(), name='licencias'),
    path('mantenimiento/', MantenimientoView.as_view(), name='listamantenimiento'),
    path('mantenimiento/<int:pk>/', MantenimientoDetailView.as_view(), name='mantenimiento'),
    path('recursos/', RegistrarMapaView.as_view(), name='listarecursos'),
    path('recursos/<int:pk>/', RegistrarMapaDetailView.as_view(), name='listarecursos'),
    path('impresora/', RegistrarImpresoraView.as_view(), name='listadocumento'),
    path('impresora/<int:pk>/', RegistrarImpresoraDetailView.as_view(), name='documento'),
    path('registrarequipo/total', views.total_equipos, name='total_equipos'),
    path('registrarusuario/total', views.total_usuarios, name='total_usuarios'),
    path('registrarlicencia/total', views.total_licencias, name='total_licencias')
]