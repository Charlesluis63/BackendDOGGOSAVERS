from rest_framework.serializers import ModelSerializer
from .models import Mascota


class Mascotaserialize(ModelSerializer):
    class Meta:
        model =  Mascota
        #No veo necesario agregar contraseña
        fields = ('id','username','estado','tipo_usuario')

