from django import forms
from . import models

class crearSolicitud(forms.ModelForm):
    class Meta:
        model = models.Solicitudes
        fields = ['descripcion', 'ubicacion']

class seguirSolicitud(forms.ModelForm):
    class Meta:
        model = models.Seguimiento
        fields = ['area','comentario']