from django.urls import path
from . import views

urlpatterns = [
    path('seleccionar_tarjeta/', views.seleccionar_tarjeta, name='seleccionar_tarjeta'),
    
]