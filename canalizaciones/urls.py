from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import SolicitudViewSet

# Configuración del router para la API REST
router = DefaultRouter()
router.register(r'api/solicitudes', SolicitudViewSet)

# Configuración de las rutas
urlpatterns = [
    path('', views.listar_solicitudes, name='listar_solicitudes'),
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('crear-alumno/', views.crear_alumno, name='crear_alumno'),
]

# Añadir las rutas del router al urlpatterns
urlpatterns += router.urls
