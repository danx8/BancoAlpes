from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    pais = models.CharField(max_length=100) 
    ciudad = models.CharField(max_length=100)
    celular = models.CharField(max_length=12)
    correo = models.CharField(max_length=100)
    
   
  
    def __str__(self):
        return f"{self.nombre, self.apellido}"
    
