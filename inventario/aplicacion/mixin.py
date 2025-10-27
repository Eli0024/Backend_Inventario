
from .middleware import get_empresa_actual
from rest_framework.exceptions import ValidationError, PermissionDenied 

class EmpresaAutoAsignadaMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        empresa_actual = get_empresa_actual(self.request)

        if empresa_actual and hasattr(queryset.model, 'empresa'):
            return queryset.filter(empresa=empresa_actual)
        

        return queryset if not hasattr(queryset.model,"empresa") else queryset.none() 

    def perform_create(self, serializer):
        empresa_actual = get_empresa_actual(self.request)

        if not empresa_actual and serializer.Meta.model.__name__ != 'RegistrarColaborador':
            raise ValidationError("Debe seleccionar una empresa válida antes de crear registros")

        models_fields = [field.name for field in serializer.Meta.model._meta.get_fields()]

        if "empresa" in models_fields and serializer.Meta.model.__name__ != 'RegistrarColaborador':
            serializer.save(empresa=empresa_actual)
        else:
            serializer.save()

    def perform_update(self, serializer):
        empresa_actual = get_empresa_actual(self.request)
        instance = self.get_object()

        if hasattr(instance, "empresa") and instance.empresa != empresa_actual:
            raise PermissionDenied("Este registro no pertenece a la empresa actual")

        serializer.save(empresa=empresa_actual)

    def perform_destroy(self, instance):
        empresa_actual = get_empresa_actual(self.request)

        if hasattr(instance, "empresa") and instance.empresa != empresa_actual:
            raise PermissionDenied("Este registro no pertenece a la empresa actual")

        instance.delete()    