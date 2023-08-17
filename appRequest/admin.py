from django.contrib import admin
from .models import Producto, Solicitudes, Seguimiento

# Register your models here.
admin.site.register(Producto)
admin.site.register(Solicitudes)
admin.site.register(Seguimiento)