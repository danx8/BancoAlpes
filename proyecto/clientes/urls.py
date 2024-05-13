from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='clienteList'),
    path('account/', views.cliente_account, name='account'),
    path('crearTarjeta/', views.cliente_tarjeta, name='crearTarjeta'),
    path('creandoTarjeta/<int:password>/', csrf_exempt(views.cliente_create_tarjeta), name='creandoTarjeta'),
    path('clienteFailed/', views.cliente_list, name='clienteFailed'),
    path('clientecreate/', csrf_exempt(views.cliente_create), name='clienteCreate'),
    path('clienteCreateFailed/', csrf_exempt(views.cliente_create), name='clienteCreateFailed'),
    path('clienteEdit/<int:cliente_id>/', csrf_exempt(views.cliente_edit), name='clienteEdit'),
    path('clienteBorrar/<int:cliente_id>/', views.cliente_borrar, name='clienteBorrar'),
    path('clienteEditSave/', csrf_exempt(views.cliente_edit), name='clienteEditSave'),
    path('clientecreate-jmeter/', csrf_exempt(views.cliente_create_jmeter), name='cliente_create_jmeter'),
    path('infoAdicionalcreate/', csrf_exempt(views.informacion_adicional_create), name='infoAdicionalcreate'),
    path('', include('adicionales.urls')),
]