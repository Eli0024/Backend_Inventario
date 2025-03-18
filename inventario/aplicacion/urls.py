from django.urls import path
from . import views 
from .views import ( RegistrarColaboradorDetailView, RegistrarColaboradorView, RegistrarEquipoView, RegistrarLicenciaView,MantenimientoView,
RegistrarImpresoraView, RegistrarEquipoDetailView, RegistrarLicenciaDetailView,
RegistrarImpresoraDetailView, MantenimientoDetailView, RegistrarPerifericoDetailView, RegistrarPerifericoView, generar_reporte_usuarios_por_area )

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
    path('impresora/', RegistrarImpresoraView.as_view(), name='listadocumento'),
    path('impresora/<int:pk>/', RegistrarImpresoraDetailView.as_view(), name='documento'),
    path('periferico/', RegistrarPerifericoView.as_view(), name='listadocumento'),
    path('periferico/<int:pk>/', RegistrarPerifericoDetailView.as_view(), name='documento'),
    path('registrarequipo/total', views.total_equipos, name='total_equipos'),
    path('registrarcolaborador/total', views.total_colaboradores, name='total_colaboradores'),
    path('registrarlicencia/total', views.total_licencias, name='total_licencias'),
    path('impresora/total', views.total_impresoras, name='total_impresoras'),
    path('mantenimiento/total', views.total_mantenimientos, name='total_mantenimientos'),
    path('periferico/total', views.total_perifericos, name='total_perificos'),

]