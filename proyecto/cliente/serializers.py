from rest_framework import serializers
from . import models


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('nombre', 'apellido', 'cedula', 'pais', 'ciudad', 'celular','correo')
        model = models.Cliente