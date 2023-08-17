from rest_framework import serializers
from .models import Producto, Solicitudes

class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitudes
        fields = ['request_id', 'descripcion', 'ubicacion', 'activo']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']
