from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import (
    RegistrarEquipoSerializer,
    RegistrarUsuarioSerializer,
    RegistrarLicenciaSerializer,
    RegistrarMapaSerializer,
    MantenimientoSerializer,
    DocumentoSerializer
)
from .models import RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, RegistrarMapa, Mantenimiento, Documento

# Create your views here.

class RegistrarEquipoView(generics.ListCreateAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarUsuarioView(generics.ListCreateAPIView):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarMapaView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarMapaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarLicenciaView(generics.ListCreateAPIView):
    queryset = RegistrarLicencia.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]        


class RegistrarEquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarLicenciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarLicencia.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]


class MantenimientoView(generics.ListCreateAPIView):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [permissions.AllowAny]


class MantenimientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [permissions.AllowAny]


class DocumentoView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [permissions.AllowAny]


class DocumentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [permissions.AllowAny]
