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
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

@login_required
def cliente_list(request):
    role = getRole(request)
    if role != "Administrador" and role != "Normal":
        form = ClienteForm()
        context = {
            'form': form,
        }
        return render(request, 'Cliente/clienteFailed.html', context)
     
          
    clientes = get_cliente()
    context = {
            'cliente_list': clientes
    }
    return render(request, 'Cliente/clientes.html', context)


@login_required
def cliente_create(request):
    role = getRole(request)
    if role != "Administrador":
        form = ClienteForm()

        context = {
            'form': form,
        }
        return render(request, 'Cliente/clienteCreateFailed.html', context)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cliente')
            #return redirect(reverse('cliente_list'))

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
def cliente_edit(request, cliente_id):
    # Obtener el cliente que se desea editar
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    role = getRole(request)
    
    # Verificar si el usuario tiene permisos de Administrador
    if role != "Administrador":
        return render(request, 'Cliente/clienteEditFailed.html')
    
    if request.method == 'POST':
        # Rellenar el formulario con los datos del cliente existente
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            # Guardar los cambios si el formulario es válido
            form.save()
            messages.success(request, 'Cliente updated successfully')
            form = ClienteForm()
            context = {
                'form': form,
            }
            
            
            
            return render(request, 'Cliente/clienteEditSave.html', context)
    else:
        # Si no es una solicitud POST, mostrar el formulario con los datos del cliente
        form = ClienteForm(instance=cliente)
    
    context = {
        'form': form,
        'cliente': cliente,
    }
    return render(request, 'Cliente/clienteEdit.html', context)


@login_required
def cliente_borrar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    role = getRole(request)
    
    if role != "Administrador":
        return render(request, 'Cliente/clienteDeleteFailed.html')
    
    if request.method == 'GET':
        # Verificar que se esté usando el método POST
        cliente.delete()
        messages.success(request, 'Cliente deleted successfully')
        return redirect("clienteList")

    else:
        context = {
            'cliente': cliente,
        }
        return render(request, 'Cliente/clienteBorrar.html', context)



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
