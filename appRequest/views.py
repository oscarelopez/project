from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from .models import Usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Solicitudes
from .serializers import SolicitudesSerializer
from . import forms

def home_view(request):
    return render(request, 'home.html')

def testPage_view(request):
    return render(request, 'test.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('test')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return redirect('home')
    #if request.method == 'POST':
    #        logout(request)
    #        return redirect('home')

@login_required(login_url='login')
def CrearSolicitudesView(request):
    solicitudes = Solicitudes.objects.filter(activo=True, usuario=request.user)
    if request.method == 'POST':
        form = forms.crearSolicitud(request.POST)
        if form.is_valid():
            # save request to db
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            #print(solicitud)
            #return redirect('home')
            return render(request, 'solicitud_crear.html',{'form':form,'solicitudes':solicitudes})
    else:
        form = forms.crearSolicitud()
        return render(request, 'solicitud_crear.html',{'form':form,'solicitudes':solicitudes})

@login_required(login_url='login')
def SeguimientoView(request):
    solicitudes = Solicitudes.objects.filter(activo=True, usuario=request.user)
    if request.method == 'POST':
        form = forms.seguirSolicitud(request.POST)
        if form.is_valid():
            id_solicitud = request.POST.get("id_solicitud")
            solicitud = Solicitudes.objects.get(pk=id_solicitud)
            seguimiento = form.save(commit=False)
            seguimiento.id_solicitud = solicitud
            seguimiento.save()
            solicitud.status = "En proceso"
            solicitud.save()
            return render(request, 'solicitud_seguir.html',{'form':form,'solicitudes':solicitudes})
    else:
        form = forms.seguirSolicitud()
        return render(request, 'solicitud_seguir.html',{'form':form,'solicitudes':solicitudes})

class SolicitudesListaView(APIView):
    def get(self, request):
        solicitud = Solicitudes.objects.filter(activo=True)
        serializer = SolicitudesSerializer(solicitud, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SolicitudesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitudesDetalleView(APIView):
    def get_object(self, pk):
        try:
            return Solicitudes.objects.get(pk=pk)
        except Solicitudes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud)
        return Response(serializer.data)

    def put(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudesSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)