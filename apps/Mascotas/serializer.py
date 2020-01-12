from rest_framework.serializers import ModelSerializer
from .models import *


class Mascotaserialize(ModelSerializer):
    class Meta:
        model =  Mascota
        #No veo necesario agregar contraseña
        fields = ('id','tipo_mascota','nombre','sexo','altura','peso','imagen','detalles','edad_aproximada')

class Mascota_adopcion_serialize (ModelSerializer):
    class Meta:
        model= Mascota_En_Adopcion
        fields = ('id','id_mascota','id_user','puntaje_juego')
