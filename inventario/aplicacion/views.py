from django.shortcuts import get_object_or_404, render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .serializers import (
    ConexionSerializer,
    RegistrarColaboradorSerializer,
    userSerializer,
    NodoSerializer,
    RegistrarEquipoSerializer,
    RegistrarUsuarioSerializer,
    RegistrarLicenciaSerializer,
    MapaSerializer,
    MantenimientoSerializer,
    ImpresoraSerializer,
    SwitchSerializer
)
from .models import Conexion, Nodo, RegistrarColaborador, RegistrarEquipo, RegistrarUsuario, RegistrarLicencia, RegistrarMapa, Mantenimiento, Impresora, Switch
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token  # Asegúrate de importar el serializer correcto
from django.contrib.auth.hashers import make_password


class RegisterViewSet(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer

    def post(self, request):
        # Serializamos los datos enviados en la petición
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            # Creamos un usuario con los datos validados
            user = serializer.save()

            # Creamos el token de autenticación para el nuevo usuario
            token = Token.objects.create(user=user)

            # Retornamos el token y los datos del usuario
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

        # Si la validación falla, retornamos los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        # Intentar obtener al usuario por el username
        try:
            user = RegistrarUsuario.objects.get(username=request.data['username'])
        except RegistrarUsuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Verificar si la contraseña es correcta
        if not user.check_password(request.data['password']):
            return Response({'error': 'Contraseña inválida'}, status=status.HTTP_400_BAD_REQUEST)

        # Crear o recuperar el token de autenticación
        token, created = Token.objects.get_or_create(user=user)

        # Serializar la información del usuario
        serializer = userSerializer(user)

        # Responder con el token y los datos del usuario
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
    

class RegistrarUsuarioViewSet(generics.ListCreateAPIView):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permissions_classes =[permissions.AllowAny]

class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarEquipoView(generics.ListCreateAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.AllowAny]
    # parser_classes = (MultiPartParser, FormParser)


class RegistrarColaboradorView(generics.ListCreateAPIView):
    queryset = RegistrarColaborador.objects.all()
    serializer_class = RegistrarColaboradorSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarMapaView(generics.ListCreateAPIView):
    queryset = RegistrarMapa.objects.all()
    serializer_class = MapaSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarMapaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarMapa.objects.all()
    serializer_class = MapaSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarLicenciaView(generics.ListCreateAPIView):
    queryset = RegistrarLicencia.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]        


class RegistrarEquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [IsAuthenticated] 
    # parser_classes = (MultiPartParser, FormParser)


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


class RegistrarColaboradorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarColaborador.objects.all()
    serializer_class = RegistrarColaboradorSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        usuario = RegistrarColaborador.objects.get(pk=pk)
        serializer = RegistrarColaboradorSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = RegistrarColaborador.objects.get(pk=pk)
        serializer = RegistrarColaboradorSerializer(usuario, data=request.data)
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


    def get(self, request, pk, format=None):
        mantenimiento = Mantenimiento.objects.get(pk=pk)
        serializer = MantenimientoSerializer(mantenimiento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mantenimiento = Mantenimiento.objects.get(pk=pk)
        serializer = MantenimientoSerializer(mantenimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrarImpresoraView(generics.ListCreateAPIView):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    permission_classes = [permissions.AllowAny]


class RegistrarImpresoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    permission_classes = [permissions.AllowAny]

class NodoViewSet(viewsets.ModelViewSet):
    queryset = Nodo.objects.all()
    serializer_class = NodoSerializer

class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer

class ConexionViewSet(viewsets.ModelViewSet):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer

# inventario/views.py
from django.http import JsonResponse

def total_equipos(request):
    # Obtén el total de equipos
    total = RegistrarEquipo.objects.count()
    return JsonResponse(total, safe=False)

def total_usuarios(request):
    # Obtén el total de equipos
    total = RegistrarUsuario.objects.count()
    return JsonResponse(total, safe=False)

def total_licencias(request):
    # Obtén el total de equipos
    total = RegistrarLicencia.objects.count()
    return JsonResponse(total, safe=False)