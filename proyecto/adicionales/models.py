from django.db import models

class Adicional(models.Model):
    cedula = models.CharField(max_length=10)
    profesion = models.CharField(max_length=100)
    actEconomica  = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ingresos = models.FloatField()
    egresos = models.FloatField( )
    deudas= models.FloatField( )
    def __str__(self):
        return '%s %s' % (self.profesion, self.empresa)