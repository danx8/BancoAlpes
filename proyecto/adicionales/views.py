from django.shortcuts import render
from .forms import AdicionalForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_adicional import create_adicional, get_adicionales

def adicional_list(request):
    adicionales = get_adicionales()
    context = {
        'adiciones_list': adicionales
    }
    return render(request, 'Adicional/adicionales.html', context)

def adicional_create(request):
    if request.method == 'POST':
        form = AdicionalForm(request.POST)
        if form.is_valid():
            create_adicional(form)
            messages.add_message(request, messages.SUCCESS, 'Adicional create successful')
            return HttpResponseRedirect(reverse('adicionalCreate'))
        else:
            print(form.errors)
    else:
        form = AdicionalForm()

    context = {
        'form': form,
    }

    return render(request, 'Adicional/adicionalCreate.html', context)

