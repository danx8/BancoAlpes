from django import forms

class TarjetaForm(forms.Form):
    TARJETAS_CHOICES = (
        ('tarjeta1', 'Tarjeta 1 (Estándar, Visa, Cupo 1000)'),
        ('tarjeta2', 'Tarjeta 2 (Oro, Mastercard, Cupo 2000)'),
        ('tarjeta3', 'Tarjeta 3 (Estándar, Mastercard, Cupo 2000)'),
    )
    
    tarjeta = forms.ChoiceField(choices=TARJETAS_CHOICES, widget=forms.RadioSelect)

    