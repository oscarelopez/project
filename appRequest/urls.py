from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ProductoListaView.as_view(), name='lista_productos'),
    #path('<int:pk>', views.ProductoDetalleView.as_view(), name='detalle_productos'),
    path('', views.SolicitudesListaView.as_view(), name='lista_solicitudes'),
    path('<int:pk>', views.SolicitudesDetalleView.as_view(), name='detalle_solicitudes'),
]