import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import Usuarioserialize,Personaserialize
from .models import Persona,Usuario
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from apps.Mascotas.models import MascotaEnAdopcion
from apps.Mascotas.models import MascotaPerdidaEncontrada

@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'persona': reverse('persona-list', request=request, format=format),
        'usuario': reverse('usuario-list', request=request, format=format),
    })

# Create your views here.

class Usuario_List(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserialize

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Usuario.objects.all()
        mascota = self.request.query_params.get('mascota', None)
        tipo = self.request.query_params.get('tipo', None)

        if mascota is not None:
            if tipo == "ADOP":
                temp3=[]
                temp=MascotaEnAdopcion.objects.all()
                temp2=Usuario.objects.all()
                for ob in temp:
                    for ob2 in temp2:
                        num=ob.id_user.id

                        if (num==ob2.id) and (int(mascota)==ob.id_mascota.id):
                            temp3.append(ob2.id)
                queryset=temp2.filter(id__in=temp3)

            if tipo == "P/E":
                print("Entro")
                temp3=[]
                temp=MascotaPerdidaEncontrada.objects.all()
                temp2=Usuario.objects.all()
                for ob in temp:
                    for ob2 in temp2:
                        num=ob.id_user.id
                        print(ob.id_user)
                        if (num==ob2.id) and (int(mascota)==ob.id_mascota.id):
                            temp3.append(ob2.id)
                queryset=temp2.filter(id__in=temp3)

        return queryset

class Usuario_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Usuario.objects.all()
    serializer_class = Usuarioserialize

class Persona_List(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = Personaserialize


class Persona_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Persona.objects.all()
    serializer_class = Personaserialize