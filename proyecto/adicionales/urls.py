from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('adicionales/', views.adicional_list),
    path('adicionalcreate/', csrf_exempt(views.adicional_create), name='adicionalCreate'),
]