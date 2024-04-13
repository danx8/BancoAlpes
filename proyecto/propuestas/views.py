from django.shortcuts import render
from .forms import TarjetaForm

def seleccionar_tarjeta(request):
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta_seleccionada = form.cleaned_data['tarjeta']
            # Aquí puedes realizar acciones basadas en la tarjeta seleccionada
            return render(request, 'resultado.html', {'tarjeta_seleccionada': tarjeta_seleccionada})
    else:
        form = TarjetaForm()

    return render(request, 'seleccionar_tarjeta.html', {'form': form})