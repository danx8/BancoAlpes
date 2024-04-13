from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'cedula',
            'pais',
            'ciudad',
            'celular',
            'correo',
            
        ]

        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'cedula' : 'Cedula',
            'pais' : 'Pais',
            'ciudad' : 'Ciudad',
            'celular' : 'Celular',
            'correo' : 'Correo',
            
        }