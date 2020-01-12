from rest_framework.serializers import ModelSerializer
from .models import *
class Personaserialize(ModelSerializer):
    class Meta:
        model =  Persona
        fields = ('cedula','nombre','apellidos','correo','numero_contacto','domicilio')

class Usuarioserialize(ModelSerializer):
    class Meta:
        model =  Usuario    
        fields = ('id','username','password','estado','tipo_usuario','persona_id')


class Persona_serialize(ModelSerializer):
    class Meta:
        model = Persona
        fields = ('cedula','nombre','apellidos','correo','numero_contacto','domicilio')