from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='clienteList'),
    path('clientecreate/', csrf_exempt(views.cliente_create), name='clienteCreate'),
    path('/clientecreate-jmeter/', csrf_exempt(views.cliente_create_jmeter), name='cliente_create_jmeter'),
    path('infoAdicionalcreate/', csrf_exempt(views.informacion_adicional_create), name='infoAdicionalcreate'),
    path('', include('adicionales.urls')),
]