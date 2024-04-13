from django import forms
from .models import Adicional

class AdicionalForm(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = [
            'cedula',
            'profesion',
            'actEconomica',
            'empresa',
            'ingresos',
            'egresos',
            'deudas',
           
        ]

        labels = {
            'cedula' : 'Cedula',
            'profesion' : 'Profesion',
            'actEconomica' : 'ActEconomica',
            'empresa' : 'Empresa',
            'ingresos' : 'Ingresos',
            'egresos' : 'Egresos',
            'deudas' : 'Deudas',
            
        }
