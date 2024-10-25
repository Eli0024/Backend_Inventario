from django.urls import path
from . import views
from .views import 

urlpatterns = [
    path('registrarequipo/', views.lista_user, name="listausuarios"),
    path('registrarequipo/<int:pk>/', views.actualizar_Usuario, name="modificarusuario"),
    path('usuarios/', RegistrarGalponView.as_view(), name='galpon_list'),
    path('registrarusuario/<int:pk>/', views.eliminar_usuarios, name="modificarusuario"),
    path('licencias/', RegistrarGranjaView.as_view(), name='granja_list'),
    path('licencias/<int:pk>/', RegistrarGalponDetailView.as_view(), name='galpon_detail'),
]