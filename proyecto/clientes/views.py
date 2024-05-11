from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClienteForm, InformacionAdicionalForm
from .models import Cliente, InformacionAdicional
from .logic.cliente_logic import get_cliente, create_cliente
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from proyecto.auth0backend import getRole

@login_required
def cliente_list(request):
    role = getRole(request)
    if role != "Administrador" and role != "Normal":
         return HttpResponse("No autorizado a listar clientes")
          
    clientes = get_cliente()
    context = {
            'cliente_list': clientes
    }
    return render(request, 'Cliente/clientes.html', context)


@login_required
def cliente_create(request):
    role = getRole(request)
    if role != "Administrador":
         return HttpResponseRedirect(reverse('clienteCreateFailed'))
    
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


def cliente_create_jmeter(request):
    
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






@login_required
def informacion_adicional_create(request, cliente_id):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    
    
    cliente = Cliente.objects.get(pk=cliente_id)
    if request.method == 'POST':
        form = InformacionAdicionalForm(request.POST)
        if form.is_valid():
            informacion = form.save(commit=False)
            informacion.cliente = cliente
            informacion.save()
            return redirect('cliente_list')  # Redirige a la lista de clientes o a otra vista
    else:
        form = InformacionAdicionalForm()
    return render(request, 'cliente/informacionAdicionalCreate.html', {'form': form})
