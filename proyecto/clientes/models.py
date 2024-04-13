from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    cedula = models.CharField(max_length=10, default='')
    celular = models.CharField(max_length=12, default='')
    correo = models.CharField(max_length=100, default='')
    pais = models.CharField(max_length=100, default='')
    ciudad = models.CharField(max_length=100, default='')
    fechaNacimiento = models.DateField()
   

    def __str__(self):
        return '{}'.format(self.cedula)
    
class InformacionAdicional(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=100)
    actEconomica = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ingresos = models.FloatField(default=0)
    egresos = models.FloatField(default=0)
    deuda = models.FloatField(default=0)

    def __str__(self):
        return f"Información adicional de {self.cliente.nombre} {self.cliente.apellido}"
    


