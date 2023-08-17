from django.db import models
from django.contrib.auth.models import User
import uuid

class Solicitudes(models.Model):
    request_id = models.UUIDField(default = uuid.uuid4, editable = False)
    descripcion = models.CharField(max_length=600)
    ubicacion = models.CharField(max_length=100)
    fecha_alta = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    status = models.CharField(max_length=100, default='Enviada')
    usuario = models.ForeignKey(User,verbose_name='usuario',on_delete=models.CASCADE,
                                related_name='fk_solicitudes_usuario',null=True,blank=True)
    
    def __str__(self):
        return str(self.request_id)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    
    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now=True)
    archivos = models.FileField(upload_to='archivos/', max_length=300, default='archivos/terminos_y_Condiciones_registro.pdf')
    activo = models.BooleanField(default=True)

    
    def __str__(self):
        return str(self.nombre)

class Seguimiento(models.Model):
    id_solicitud = models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    comentario = models.CharField(max_length=500)

#class Persona(models.Model):
#    ESTADOS = [ ('Chihuahua','Chihuahua'), ("Jalisco","Jalisco"), ("Michoacan","Michoacan")]
#    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#    nombre = models.CharField(max_length=100)
#    apellidos = models.CharField(max_length=100)
#    edad = models.IntegerField()
#    calle = models.CharField(max_length=100)
#    colonia = models.CharField(max_length=100)
#    codigo_postal = models.CharField(max_length=5)
#    estado = models.CharField(max_length=100, choices=ESTADOS)
#    activo = models.BooleanField(default=True)
    
#    def __str__(self):
#        return str(self.nombre)

# Create your models here.

#class Member(models.Model):
#  firstname = models.CharField(max_length=255)
#  lastname = models.CharField(max_length=255)
