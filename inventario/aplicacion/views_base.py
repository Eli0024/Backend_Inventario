from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .middleware import get_empresa_actual

class EmpresaFilteredViewMixin:
    """
    Mixin para filtrar automáticamente por empresa en las vistas
    """
    
    def get_queryset(self):
        queryset = super().get_queryset()
        empresa_actual = get_empresa_actual(self.request)
        
        if empresa_actual:
            if hasattr(queryset.model, 'empresa'):
                return queryset.filter(empresa=empresa_actual)
        
        # Si no hay empresa seleccionada, retornar queryset vacíao
        return queryset.none()
    
    def perform_create(self, serializer):
        empresa_actual = get_empresa_actual(self.request)

        if not empresa_actual:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("Debe seleccionar una empresa válida antes de crear registros")
        
        if  hasattr(serializer.Meta.model, 'empresa'):
            serializer.save(empresa=empresa_actual)
        else:
            serializer.save()

class EmpresaFilteredListCreateView(EmpresaFilteredViewMixin, generics.ListCreateAPIView):
    """
    Vista base para listar y crear objetos filtrados por empresa
    """
    pass

class EmpresaFilteredRetrieveUpdateDestroyView(EmpresaFilteredViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Vista base para obtener, actualizar y eliminar objetos filtrados por empresa
    """
    pass

class AdminOnlyMixin:
    """
    Mixin para restringir acceso solo a administradores
    """
    
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Solo los administradores pueden crear este recurso")
        super().perform_create(serializer)
    
    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Solo los administradores pueden modificar este recurso")
        super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Solo los administradores pueden eliminar este recurso")
        super().perform_destroy(instance) 