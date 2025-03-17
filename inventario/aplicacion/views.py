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
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from aplicacion.models import RegistrarUsuario  # Asegúrate de importar tu modelo personalizado
from rest_framework import generics, permissions, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import PermissionDenied

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = RegistrarUsuario.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def login(request):
    user = request.user
    if not user:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': {
            'username': user.username,
            'is_staff': user.is_staff
        }
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, Token.DoesNotExist):
        pass

    response = Response({'message': 'Logged out successfully'})
    response.delete_cookie('token')
    return response

class RegistrarEquipoView(generics.ListCreateAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")

class RegistrarEquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarEquipo.objects.all()
    serializer_class = RegistrarEquipoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Equipo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def equipo_por_colaborador(request, id_colaborador):
    try:
        equipos = RegistrarEquipo.objects.filter(responsable_id=id_colaborador)
        if equipos.exists():
            equipo = equipos.first()
            serializer = RegistrarEquipoSerializer(equipo, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "No se encontró ningún equipo para este colaborador"},
                status=status.HTTP_404_NOT_FOUND
            )
    except Exception as e:
        return Response(
            {"error": f"Error del servidor: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
from django.http import HttpResponse
from openpyxl import Workbook


from django.http import HttpResponse
from openpyxl import Workbook


def generar_reporte_usuarios_por_area(request):
    # Obtener el área desde los parámetros de la solicitud
    area = request.GET.get('area', None)

    if not area:
        return HttpResponse("Debes proporcionar un área.", status=400)

    # Filtrar los usuarios por área
    usuarios = RegistrarColaborador.objects.filter(area=area)

    if not usuarios.exists():
        return HttpResponse("No se encontraron usuarios para el área especificada.", status=404)

    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Usuarios y Equipos por Área"

    # Agregar encabezados
    worksheet.append([
        "ID Usuario", "Nombre", "Apellido", "Área", "Cargo", "Empresa",  # Datos del usuario
        "ID Equipo", "Marca", "Modelo", "Memoria", "Procesador", "Office", "Serial", "Sistema Operativo", "Fecha Adquisición", "Estado"  # Datos del equipo
    ])

    # Agregar datos de los usuarios y sus equipos
    for usuario in usuarios:
        # Obtener el equipo asociado al usuario (suponiendo una relación uno a uno)
        equipo = RegistrarEquipo.objects.filter(responsable=usuario).first()

        worksheet.append([
            # Datos del usuario
            usuario.id_colaborador,
            usuario.nombre,
            usuario.apellido,
            usuario.area,
            usuario.cargo,
            usuario.empresa,
            # Datos del equipo (si existe)
            equipo.id_equipo if equipo else "N/A",
            equipo.marca if equipo else "N/A",
            equipo.modelo if equipo else "N/A",
            equipo.memoria if equipo else "N/A",
            equipo.procesador if equipo else "N/A",
            equipo.office if equipo else "N/A",
            equipo.serial if equipo else "N/A",
            equipo.sistema_operativo if equipo else "N/A",
            equipo.fecha_adquisicion if equipo else "N/A",
            equipo.estado if equipo else "N/A",
        ])

    # Crear una respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=usuarios_y_equipos_{area}.xlsx'

    # Guardar el libro de Excel en la respuesta
    workbook.save(response)

    return response

class RegistrarUsuarioViewSet(generics.ListCreateAPIView):
     queryset = RegistrarUsuario.objects.all()
     serializer_class = RegistrarUsuarioSerializer
     permissions_classes =[permissions.AllowAny]

     def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")

class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = RegistrarUsuario.objects.all()
     serializer_class = RegistrarUsuarioSerializer
     permission_classes = [permissions.AllowAny]

     def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()


class RegistrarColaboradorView(generics.ListCreateAPIView):
    queryset = RegistrarColaborador.objects.all()
    serializer_class = RegistrarColaboradorSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")

class RegistrarMapaView(generics.ListCreateAPIView):
    queryset = RegistrarMapa.objects.all()
    serializer_class = MapaSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")


class RegistrarMapaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistrarMapa.objects.all()
    serializer_class = MapaSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()

class RegistrarLicenciaView(generics.ListCreateAPIView):
    queryset = RegistrarLicencia.objects.all()
    serializer_class = RegistrarLicenciaSerializer
    permission_classes = [permissions.AllowAny]        

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")


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
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()


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
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()

class MantenimientoView(generics.ListCreateAPIView):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo los administradores pueden crear productos")
        
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

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()
    
class RegistrarImpresoraView(generics.ListCreateAPIView):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    permission_classes = [permissions.AllowAny]

    

class RegistrarImpresoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar productos")
        return super().get_permissions()


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

def total_mantenimiento(request):
    # Obtén el total de equipos
    total = Mantenimiento.objects.count()
    return JsonResponse(total, safe=False)

def total_impresoras(request):
    # Obtén el total de equipos
    total = Impresora.objects.count()
    return JsonResponse(total, safe=False)

# def total_licencias(request):
#     # Obtén el total de equipos
#     total = RegistrarLicencia.objects.count()
#     return JsonResponse(total, safe=False)