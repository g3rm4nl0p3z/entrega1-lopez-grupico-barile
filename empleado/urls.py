from django.urls import path
from empleado.views import ver_empleados, crear_empleado, buscar_empleados

urlpatterns = [
    path('', ver_empleados, name="ver-empleados"),
    path('nuevo/', crear_empleado, name="crear-empleado"),
    path('buscar/', buscar_empleados, name="buscar-empleados"),
]
