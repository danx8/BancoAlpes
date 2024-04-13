from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClienteForm
from .logic.cliente_logic import get_cliente, create_cliente

def cliente_list(request):
    clientes = get_cliente()
    context = {
        'cliente_list': clientes
    }
    return render(request, 'Cliente/clientes.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cliente')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }
    return render(request, 'Cliente/clienteCreate.html', context)


