from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_clientes import create_cliente, get_clientes

def clientes_list(request):
    clientes = get_clientes()
    context = {
        'clientes_list': clientes
    }
    return render(request, 'clientes.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'Cliente create successful')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'clienteCreate.html', context)