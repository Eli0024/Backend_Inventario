from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from .models import Empresa

class EmpresaMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        print(">>>> Entró al middleware")
        request.empresa_actual = None
           

        empresa_id = request.headers.get('X-Empresa-ID') or request.GET.get('empresa')
        print(">>> HEADER X-Empresa-ID:", empresa_id)

        if empresa_id:
                try:
                    empresa = Empresa.objects.get(id=int(empresa_id), activa=True)
                    print(">>> Empresa encontrada",empresa.nombre)
                    request.empresa_actual = empresa
                except Empresa.DoesNotExist:
                    print(">>>Empresa no encontrada")
                    return JsonResponse({'error': 'Empresa no encontrada o inactiva'}, status=400)

def get_empresa_actual(request):
    """
    Función  para obtener la empresa actual
    """
    return getattr(request, 'empresa_actual', None) 