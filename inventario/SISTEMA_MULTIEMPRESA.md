# Sistema Multiempresa - Documentación

## Descripción General

Este sistema permite que los usuarios se registren en una empresa específica, pero puedan acceder y trabajar con datos de diferentes empresas según sus permisos.

## Flujo de Funcionamiento

### 1. Registro de Usuario
- El usuario se registra especificando:
  - Username
  - Password
  - Si es administrador o no

### 2. Login
- El usuario inicia sesión con:
  - Username
  - Password
  - Empresa con la que quiere trabajar (opcional)

### 3. Cambio de Empresa
- Una vez autenticado, el usuario puede cambiar de empresa usando el endpoint `/cambiar-empresa/`
- Se debe enviar el `empresa_id` en el header `X-Empresa-ID` en las siguientes peticiones

## Endpoints Principales

### Autenticación
- `POST /register/` - Registro de usuario
- `POST /login/` - Inicio de sesión
- `POST /logout/` - Cierre de sesión

### Gestión de Empresas
- `GET /empresas/` - Obtener todas las empresas disponibles
- `POST /cambiar-empresa/` - Cambiar empresa de trabajo
- `GET /empresa-actual/` - Obtener empresa actual
- `GET /datos-empresa/` - Obtener estadísticas de la empresa actual

## Cómo Usar el Sistema

### 1. Registro
```json
POST /register/
{
    "username": "usuario1",
    "password": "password123",
    "is_staff": false
}
```

### 2. Login
```json
POST /login/
{
    "username": "usuario1",
    "password": "password123",
    "empresa": 2
}
```

### 3. Cambiar Empresa
```json
POST /cambiar-empresa/
{
    "empresa_id": 3
}
```

### 4. Hacer Peticiones con Empresa Específica
```http
GET /registrarequipo/
X-Empresa-ID: 3
Authorization: Token tu_token_aqui
```

## Características del Sistema

### Filtrado Automático
- Todas las vistas filtran automáticamente por empresa
- Si no se especifica empresa, se retorna lista vacía
- Los administradores pueden crear/modificar/eliminar recursos

### Seguridad
- Autenticación por token
- Validación de permisos por empresa
- Solo usuarios activos pueden acceder

### Middleware
- `EmpresaMiddleware`: Maneja automáticamente la empresa actual
- Se puede especificar empresa por header `X-Empresa-ID` o query param `empresa`

## Estructura de Archivos

- `middleware.py`: Middleware para manejo de empresa
- `views_base.py`: Clases base para vistas filtradas
- `models.py`: Modelos con campo empresa
- `views.py`: Vistas actualizadas con filtrado automático
- `urls.py`: URLs organizadas por funcionalidad

## Notas Importantes

1. Los usuarios pueden acceder a cualquier empresa activa
2. Todos los datos se filtran automáticamente por empresa
3. Los administradores tienen permisos especiales
4. El sistema es escalable y mantenible 