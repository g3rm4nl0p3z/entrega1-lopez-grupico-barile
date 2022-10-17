from django.shortcuts import render, redirect
from empleado.models import Empleado
from empleado.forms import FormularioBuscarEmpleados, FormularioEmpleado

def ver_empleados(request):
    empleados = Empleado.objects.all().order_by('id')
    return render(request, 'empleado/ver-empleados.html', {'empleados': empleados})


def crear_empleado(request):
    if request.method == 'POST':
        formulario_empleado = FormularioEmpleado(request.POST)

        if formulario_empleado.is_valid():
            datos_empleado = formulario_empleado.cleaned_data
            empleado = Empleado(
                nombre=datos_empleado['nombre'],
                apellido=datos_empleado['apellido'],
                documento=datos_empleado['documento'],
                genero=datos_empleado['genero'],
                fecha_nacimiento=datos_empleado['fecha_nacimiento'],
                email=datos_empleado['email'],
                domicilio=datos_empleado['domicilio'],
                telefono=datos_empleado['telefono']
            )

            empleado.save()
            return redirect(ver_empleados)
    else:
        formulario_empleado = FormularioEmpleado()

    return render(request, 'empleado/crear-empleado.html', {'formulario_empleado': formulario_empleado})


def buscar_empleados(request):
    empleados = None
    nombre = request.GET.get('nombre', None)
    apellido = request.GET.get('apellido', None)
    genero = request.GET.get('genero', None)

    # Filtros de búsqueda: Nombre, Apellido, Género
    if nombre or apellido or genero:
        if nombre:
            empleados = Empleado.objects.filter(nombre__istartswith=nombre)

        if apellido:
            if empleados:
                empleados = empleados.filter(apellido__istartswith=apellido)
            else:
                empleados = Empleado.objects.filter(apellido__istartswith=apellido)

        if genero:
            if empleados:
                empleados = empleados.filter(genero__exact=genero)
            else:
                empleados = Empleado.objects.filter(genero__exact=genero)

        empleados = empleados.order_by('id')

    formulario_buscar_empleados = FormularioBuscarEmpleados()

    return render(request, 'empleado/buscar-empleados.html', {'empleados': empleados, 'formulario_buscar_empleados': formulario_buscar_empleados})
