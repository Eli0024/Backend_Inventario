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

    def get(self, request, pk, format=None):
        equipo = RegistrarEquipo.objects.get(pk=pk)
        serializer = RegistrarEquipoSerializer(equipo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        equipo = RegistrarEquipo.objects.get(pk=pk)
        serializer = RegistrarEquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        usuario = RegistrarUsuario.objects.get(pk=pk)
        serializer = RegistrarUsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = RegistrarUsuario.objects.get(pk=pk)
        serializer = RegistrarUsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrarLicenciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarLicencia.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        licencia = RegistrarLicencia.objects.get(pk=pk)
        serializer = RegistrarLicenciaSerializer(licencia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        licencia = RegistrarLicencia.objects.get(pk=pk)
        serializer = RegistrarLicenciaSerializer(licencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
