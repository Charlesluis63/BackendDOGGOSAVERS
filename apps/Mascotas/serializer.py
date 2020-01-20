from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class Mascotaserialize(serializers.HyperlinkedModelSerializer):
    razas = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Raza.objects.all())
    class Meta:
        model =  Mascota
        #No veo necesario agregar contraseña
        fields = ('id','tipo_mascota','nombre','sexo','altura','peso','edad_aproximada','imagen','detalles','razas')


class Mascota_adopcion_serialize (ModelSerializer):
    class Meta:
        model= MascotaEnAdopcion
        fields = ('id','id_mascota','id_user','puntaje_juego')

class Razaserialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Raza
        #No veo necesario agregar contraseña
        fields = ('raza',)

class Mascota_Perdida_Encontrada_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  MascotaPerdidaEncontrada
        #No veo necesario agregar contraseña
        fields = ('id','id_mascota','id_user', 'estado_mascota','sector_encuentro_perdida','detalle')

class Mascota_Adoptada_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  MascotaAdoptada
        #No veo necesario agregar contraseña
        fields = ('id','id_mascota','id_user', 'fecha','hora','detalle')
