from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import Registrar_EquiposSerializer, RegistrarUsuarioSerializer, RegistrarLicenciaSerializer
from .models import RegistrarEquipo, RegistrarUsuario, RegistrarLicencia
# Create your views here.

class RegistrarEquipoView(generics.ListCreateAPIView):
    queryset = Equipos.objects.all()
    serializer_class = Registrar_EquiposSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarUsuarioView(generics.ListCreateAPIView):
    queryset =  Usuarios.objects.all()
    serializer_class = RegistrarUsuariosSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarlicenciasView(generics.ListCreateAPIView):
    queryset =  licencias.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]        

class RegistrarEquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipos.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']

class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE'] 

class RegistrarLicenciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Licencias.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']               