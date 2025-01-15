from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from .serializers import (
    ConexionSerializer,
    RegistrarColaboradorSerializer,
    NodoSerializer,
    RegistrarEquipoSerializer,
    RegistrarLicenciaSerializer,
    MapaSerializer,
    MantenimientoSerializer,
    ImpresoraSerializer,
    RegistrarUsuarioSerializer,
    SwitchSerializer,
    userSerializer
)
from .models import Conexion, Nodo, RegistrarColaborador, RegistrarEquipo, RegistrarLicencia, RegistrarMapa, Mantenimiento, Impresora, RegistrarUsuario, Switch
from rest_framework.authtoken.models import Token
from rest_framework import status,generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from aplicacion.models import RegistrarUsuario  # Asegúrate de importar tu modelo personalizado



@api_view(['POST'])
def register (request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user  = RegistrarUsuario.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate

@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Usamos el TokenAuthentication para verificar el token
@permission_classes([IsAuthenticated])  # Aseguramos que el usuario debe estar autenticado
def login(request):
    user = request.user  # Al usar TokenAuthentication, 'request.user' estará poblado automáticamente con el usuario autenticado

    # Si el usuario no está autenticado, devolveremos un error
    if not user:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

    # Generamos o recuperamos el token para el usuario (aunque si ya está autenticado, no es necesario generar uno nuevo)
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key,
        'user': {
            'username': user.username,
            'is_staff': user.is_staff
        }
    }, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(RegistrarUsuario, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = userSerializer(instance=user)
#     return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

# class LoginView(APIView):
#     authentication_classes = [TokenAuthentication]  # Usar autenticación por token
#     permission_classes = [IsAuthenticated]  # Asegurarse de que el usuario esté autenticado

#     def post(self, request):
# #         # Aquí puedes manejar la lógica de login, por ejemplo, retornando un mensaje de éxito
#        return Response({"message": "Login exitoso"})



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

def total_colaboradores(request):
    # Obtén el total de equipos
    total = RegistrarColaborador.objects.count()
    return JsonResponse(total, safe=False)

def total_licencias(request):
    # Obtén el total de equipos
    total = RegistrarLicencia.objects.count()
    return JsonResponse(total, safe=False)