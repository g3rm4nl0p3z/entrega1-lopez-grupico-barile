from django import forms

'''
    FORMULARIO EMPLEADO
        - Nombre: STRING
        - Apellido: STRING
        - Documento: INTEGER
        - Género: STRING
        - Fecha nacimiento: DATE
        - Email: STRING
        - Domicilio: STRING
        - Teléfono: INTEGER
'''
class FormularioEmpleado(forms.Form):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    documento = forms.IntegerField(required=True)
    genero = forms.CharField(max_length=1, widget=forms.Select(choices=GENERO_CHOICES), required=True)
    fecha_nacimiento = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    domicilio = forms.CharField(max_length=150, required=True)
    telefono = forms.IntegerField(required=True)


'''
    FORMULARIO BUSCAR EMPLEADOS
        - Filtro Nombre: STRING
        - Filtro Apellido: STRING
        - Filtro Género: STRING
'''
class FormularioBuscarEmpleados(forms.Form):

    GENERO_CHOICES = [
        ('', ''),
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    nombre = forms.CharField(max_length=50, required=False)
    apellido = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=1, widget=forms.Select(choices=GENERO_CHOICES), required=False)
