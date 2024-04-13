from ..models import Cliente

def create_cliente(form):
    cliente = form.save()
    cliente.save()
    return ()

def get_clientes():
    queryset = Cliente.objects.all()

    return (queryset)