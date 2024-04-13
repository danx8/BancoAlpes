from ..models import Adicional

def get_adicionales():
    queryset = Adicional.objects.all()
    return (queryset)

def create_adicional(form):
    adicional = form.save()
    adicional.save()
    return ()