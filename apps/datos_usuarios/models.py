from django.db import models

# Create your models here.
class Persona(models.Model):
    
    #DEBERIA SER LA LLAVE PRINCIPAL c
    cedula = models.CharField(max_length = 11, primary_key = True)
    nombre = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    correo = models.CharField(max_length = 25)
    numero_contacto = models.CharField(max_length = 20)
    domicilio = models.CharField(max_length = 40)

class Usuario(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    estado = models.CharField(max_length = 15)
    tipo_usuario = models.CharField(max_length = 15)
    persona = models.OneToOneField(Persona, on_delete= models.CASCADE)

