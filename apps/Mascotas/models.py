from django.db import models
from apps.datos_usuarios.models import Usuario


class Raza (models.Model):
    raza = models.CharField(max_length = 20)
    def __str__(self):
        return self.raza

class Mascota (models.Model):
    PERRO = 'PE'
    GATO =  'GA'
    LORO =  'LO'
    TIPO_MASCOTA_ELECCION = [(PERRO,'perro'),(GATO,'gato'),(LORO,'loro')]
    MACHO = 'M'
    HEMBRA = 'H'
    SEXO = [(MACHO,'macho'),(HEMBRA,'hembra')]

    tipo_mascota = models.CharField(max_length = 2, choices = TIPO_MASCOTA_ELECCION)
    nombre= models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 2, choices = SEXO)
    altura = models.DecimalField(max_digits = 4, decimal_places= 2 )
    peso = models.DecimalField(max_digits = 4, decimal_places= 2 )
    #La edad aproximada, constaria de años y meses? Lo que llevaria a hacer una transformacion segun lo que agregue el usuario
    edad_aproximada = models.DecimalField(max_digits = 4, decimal_places = 2)
    imagen = models.URLField(max_length = 100)
    detalles = models.CharField(max_length = 200)
    razas = models.ManyToManyField(Raza)

    def __str__(self):
        return self.nombre

class MascotaEnAdopcion(models.Model):
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntaje_juego = models.DecimalField(max_digits= 4, decimal_places=2)

class  MascotaAdoptada(models.Model):
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    detalle = models.CharField(max_length= 200)

class MascotaPerdidaEncontrada(models.Model):
    PERDIDO = 'PE'
    ENCONTRADO =  'EN'
    TIPO_MASCOTA_ELECCION = [(PERDIDO,'perdido'),(ENCONTRADO,'encontrado')]
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado_mascota = models.CharField(max_length = 2 , choices = TIPO_MASCOTA_ELECCION)
    #DEBE DEFINIRSE COORDENADAS, O SOLO UNA DIRECCION
    sector_encuentro_perdida = models.CharField(max_length= 50)
    detalle = models.CharField(max_length= 300) 
    
