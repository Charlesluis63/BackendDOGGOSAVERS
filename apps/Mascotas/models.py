from django.db import models

class Mascota (models.Model):
    PERRO = 'PE'
    GATO =  'GA'
    LORO =  'LO'
    TIPO_MASCOTA_ELECCION = [(PERRO,'perro'),(GATO,'gato'),(LORO,'loro')]
    tipo_mascota = models.CharField(max_length = 2, choices = TIPO_MASCOTA_ELECCION, default = PERRO)
    nombre= models.CharField(max_length = 30)
    altura = models.DecimalField(max_digits = 4, decimal_places= 2 )
    peso = models.DecimalField(max_digits = 4, decimal_places= 2 )
    edad_aproximada = models.IntegerField()
    imagen = models.URLField(max_length = 100)
    detalles = models.CharField(max_length = 200)
    razas = models.ManyToManyField(Raza)

    def __str__(self):
        return self.nombre

class Raza (models.Model):
    raza = models.CharField(max_length = 20)
    def __str__(self):
        return self.raza
        
    
