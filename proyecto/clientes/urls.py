from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='clienteList'),
    path('clienteFailed/', views.cliente_list, name='clienteFailed'),
    path('clientecreate/', csrf_exempt(views.cliente_create), name='clienteCreate'),
    path('clienteCreateFailed/', csrf_exempt(views.cliente_create), name='clienteCreateFailed'),
    path('clienteEdit/', csrf_exempt(views.cliente_create), name='clienteEdit'),
    path('clientecreate-jmeter/', csrf_exempt(views.cliente_create_jmeter), name='cliente_create_jmeter'),
    path('infoAdicionalcreate/', csrf_exempt(views.informacion_adicional_create), name='infoAdicionalcreate'),
    path('', include('adicionales.urls')),
]