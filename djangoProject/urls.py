"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from appRequest.views import home_view
from appRequest.views import testPage_view
from appRequest.views import login_view
from appRequest.views import logout_view
from appRequest.views import CrearSolicitudesView
from appRequest.views import SeguimientoView
from appRequest.views import SolicitudesListaView, SolicitudesDetalleView

urlpatterns = [
    path('', home_view, name='home'),
    path('test/', testPage_view, name='test'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("admin/", admin.site.urls),
    path('create/', CrearSolicitudesView, name='solicitudes-crear'),
    path('seguir/', SeguimientoView, name='solicitudes-seguir'),
    path('solicitudes/', SolicitudesListaView.as_view(), name='solicitudes-lista'),
    path('solicitudes/<int:pk>/', SolicitudesDetalleView.as_view(), name='solicitudes-detalle'),
    path('api/', include('appRequest.urls')),
]

#urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)