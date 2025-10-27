from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import ( 
    MantenimpreDetailView, MantenimpreView, 
    RegistrarColaboradorDetailView, RegistrarColaboradorView, RegistrarColaboradorAllView,
    RegistrarEquipoView, RegistrarEquipoDetailView,
    RegistrarLicenciaView, RegistrarLicenciaDetailView,
    RegistrarImpresoraView, RegistrarImpresoraDetailView,
    RegistrarPerifericoView, RegistrarPerifericoDetailView,
    MantenimientoView, MantenimientoDetailView,
    generar_reporte_usuarios_por_area,
    ContrasenaSiesaView, ContrasenaSiesaDetailView,
    ContrasenaAntivirusView, ContrasenaAntivirusDetailView,
    ContrasenaVPNView, ContrasenaVPNDetailView,
    ContrasenaServidorView, ContrasenaServidorDetailView,
    ContrasenaEquipoView, ContrasenaEquipoDetailView,
    RegistroTareaView, RegistroTareaDetailView,obtener_captcha, cambiar_password_con_captcha
)

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('empresas/', views.obtener_empresas_usuario, name='obtener_empresas'),
    path('empresa-actual/', views.obtener_empresa_actual, name='empresa_actual'),
    path('datos-empresa/', views.obtener_datos_empresa_filtrados, name='datos_empresa'),
    
    # Reportes
    path('api/generar-reporte/', generar_reporte_usuarios_por_area, name='generar_reporte'),
    path('registrarequipo/por-colaborador/<int:id_colaborador>/', views.equipo_por_colaborador, name='equipo_por_colaborador'),
    path('mantenimpre/por-impresora/<int:id_impresora>/', views.impresora_con_mantenimiento, name='impresora_por_manten'),
    #detalles de equipos
    path('licencias/equipo/<int:equipo_id>/', views.obtener_licencias_por_equipo, name='obtener_licencias_por_equipo'),

    path('licencias/equipo/<int:equipo_id>/', views.LicenciasPorEquipoView.as_view(), name='licencias-por-equipo'),
    path('mantenimiento/equipo/<int:equipo_id>/', views.MantenimientosPorEquipoView.as_view(), name='mantenimientos-por-equipo'),


    # Registro de tareas
    path('registro-tarea/', RegistroTareaView.as_view(), name='registro-tarea'),
    path('registro-tarea/<int:pk>/', RegistroTareaDetailView.as_view(), name='registro-tarea-detail'),

    # Equipos
    path('registrarequipo/', RegistrarEquipoView.as_view(), name="listaequipo"),
    path('registrarequipo/<int:pk>/', RegistrarEquipoDetailView.as_view(), name="registrarequipo"),

    # Colaboradores
    path('colaborador/', RegistrarColaboradorView.as_view(), name='listausuarios'),
    path('colaborador/<int:pk>/', RegistrarColaboradorDetailView.as_view(), name="colaborador-detail"),
    path('colaborador/all/', RegistrarColaboradorAllView.as_view(), name='colaboradores-todos'),
    path('colaborador/registrar/', RegistrarColaboradorView.as_view(), name="registrarusuario"),

    # Licencias
    path('licencias/', RegistrarLicenciaView.as_view(), name='listalicencia'),
    path('licencias/<int:pk>/', RegistrarLicenciaDetailView.as_view(), name='licencias'),

    # Mantenimientos
    path('mantenimiento/', MantenimientoView.as_view(), name='listamantenimiento'),
    path('mantenimiento/<int:pk>/', MantenimientoDetailView.as_view(), name='mantenimiento'),

    # Impresoras
    path('impresora/', RegistrarImpresoraView.as_view(), name='listadocumento'),
    path('impresora/<int:pk>/', RegistrarImpresoraDetailView.as_view(), name='documento'),

    # Periféricos
    path('periferico/', RegistrarPerifericoView.as_view(), name='listadocumento'),
    path('periferico/<int:pk>/', RegistrarPerifericoDetailView.as_view(), name='documento'),

    # Mantenimpre
    path('mantenimpre/', MantenimpreView.as_view(), name='listadocumento'),
    path('mantenimpre/<int:pk>/', MantenimpreDetailView.as_view(), name='documento'),

    # Eventos
    path('eventos/', views.CalendarioEventoView.as_view(), name='eventos_list_create'),
    path('eventos/<int:pk>/', views.CalendarioEventoDetailView.as_view(), name='eventos_detail'),

    # TOTALES
    path('registrarequipo/total/', views.total_equipos, name='total_equipos'),
    path('registrarcolaborador/total/', views.total_colaboradores, name='total_colaboradores'),
    path('registrarlicencia/total/', views.total_licencias, name='total_licencias'),
    path('impresora/total/', views.total_impresoras, name='total_impresoras'),
    path('mantenimiento/total/', views.total_mantenimientos, name='total_mantenimientos'),
    path('perifericos/total/', views.total_perifericos, name='total_perifericos'),
    path('contrasena-siesa/total/', views.total_contrasena_siesa, name='total_contrasena_siesa'),
    path('contrasena-antivirus/total/', views.total_contrasena_antivirus, name='total_contrasena_antivirus'),
    path('contrasena-vpn/total/', views.total_contrasena_vpn, name='total_contrasena_vpn'),
    path('contrasena-servidor/total/', views.total_contrasena_servidor, name='total_contrasena_servidor'),
    path('contrasena-equipo/total/', views.total_contrasena_equipo, name='total_contrasena_equipo'),
    
    # Contraseñas
    path('contrasena-siesa/', ContrasenaSiesaView.as_view(), name='contrasena_siesa_list'),
    path('contrasena-siesa/<int:pk>/', ContrasenaSiesaDetailView.as_view(), name='contrasena_siesa_detail'),
    path('contrasena-antivirus/', ContrasenaAntivirusView.as_view(), name='contrasena_antivirus_list'),
    path('contrasena-antivirus/<int:pk>/', ContrasenaAntivirusDetailView.as_view(), name='contrasena_antivirus_detail'),
    path('contrasena-vpn/', ContrasenaVPNView.as_view(), name='contrasena_vpn_list'),
    path('contrasena-vpn/<int:pk>/', ContrasenaVPNDetailView.as_view(), name='contrasena_vpn_detail'),
    path('contrasena-servidor/', ContrasenaServidorView.as_view(), name='contrasena_servidor_list'),
    path('contrasena-servidor/<int:pk>/', ContrasenaServidorDetailView.as_view(), name='contrasena_servidor_detail'),
    path('contrasena-equipo/', ContrasenaEquipoView.as_view(), name='contrasena_equipo_list'),
    path('contrasena-equipo/<int:pk>/', ContrasenaEquipoDetailView.as_view(), name='contrasena_equipo_detail'),

    path('captcha/', include('captcha.urls')),
    path('api/get-captcha/', obtener_captcha, name='get-captcha'),
    path('api/change-password/', cambiar_password_con_captcha, name='change-password'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
