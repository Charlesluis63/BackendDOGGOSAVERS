from rest_framework.serializers import ModelSerializer
from .models import Mascota


class Mascotaserialize(ModelSerializer):
    class Meta:
        model =  Mascota
        fields = ('nombre','tipo_mascota','sexo','razas')
