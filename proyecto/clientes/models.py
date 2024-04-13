from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    cedula = models.CharField(max_length=10, default='')
    celular = models.CharField(max_length=12, default='')
    correo = models.CharField(max_length=100, default='')
    pais = models.CharField(max_length=100, default='')
    ciudad = models.CharField(max_length=100, default='')
    fechaNacimiento = models.DateField(default='2000-01-01')
   

    def __str__(self):
        return '{}'.format(self.cedula)
    


