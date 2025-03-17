from django.urls import path
from . import views 
from .views import ( RegistrarColaboradorDetailView, RegistrarColaboradorView, RegistrarEquipoView, RegistrarLicenciaView, RegistrarMapaView, MantenimientoView,
RegistrarImpresoraView, RegistrarEquipoDetailView, RegistrarLicenciaDetailView, RegistrarMapaDetailView,
RegistrarImpresoraDetailView, MantenimientoDetailView, generar_reporte_usuarios_por_area )

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('api/generar-reporte/', generar_reporte_usuarios_por_area, name='generar_reporte'),
    path('registrarequipo/por-colaborador/<int:id_colaborador>/', views.equipo_por_colaborador, name='equipo_por_colaborador'),
    path('registrarequipo/', RegistrarEquipoView.as_view(), name="listaequipo"),
    path('registrarequipo/<int:pk>/', RegistrarEquipoDetailView.as_view(), name="registrarequipo"),
    path('colaborador/', RegistrarColaboradorView.as_view(), name='listausuarios'),
    path('colaborador/<int:pk>/', RegistrarColaboradorDetailView.as_view(), name="registrarusuario"),
    path('licencias/', RegistrarLicenciaView.as_view(), name='listalicencia'),
    path('licencias/<int:pk>/', RegistrarLicenciaDetailView.as_view(), name='licencias'),
    path('mantenimiento/', MantenimientoView.as_view(), name='listamantenimiento'),
    path('mantenimiento/<int:pk>/', MantenimientoDetailView.as_view(), name='mantenimiento'),
    path('recursos/', RegistrarMapaView.as_view(), name='listarecursos'),
    path('recursos/<int:pk>/', RegistrarMapaDetailView.as_view(), name='listarecursos'),
    path('impresora/', RegistrarImpresoraView.as_view(), name='listadocumento'),
    path('impresora/<int:pk>/', RegistrarImpresoraDetailView.as_view(), name='documento'),
    path('registrarequipo/total', views.total_equipos, name='total_equipos'),
    path('registrarcolaborador/total', views.total_colaboradores, name='total_colaboradores'),
    path('registrarlicencia/total', views.total_licencias, name='total_licencias')
]