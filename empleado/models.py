from django.db import models
from datetime import date

'''
    MODELO EMPLEADO
        - Nombre: STRING
        - Apellido: STRING
        - Documento: INTEGER
        - Género: STRING
        - Fecha nacimiento: DATE
        - Email: STRING
        - Domicilio: STRING
        - Teléfono: INTEGER
        - Fecha creación: DATETIME (Al momento del alta del empleado)
        - Fecha modificación: DATETIME (Al momento de modificar datos del empleado)
'''
class Empleado(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    domicilio = models.CharField(max_length=150)
    telefono = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)


# Método de cálculo de la edad de un empleado
    def calcular_edad(self):
        fecha_del_dia = date.today()
        edad = fecha_del_dia.year - self.fecha_nacimiento.year - ((fecha_del_dia.month, fecha_del_dia.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad
