import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new


@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'mascotas': reverse('mascotas-list', request=request, format=format),
        'razas': reverse('razas-list', request=request, format=format),
        'mascotas_adopcion': reverse('mascotasadopcion-list', request=request, format=format),
        'mascotas_perdidas_encontradas': reverse('mascota_perdida_encontrada-list', request=request, format=format),
        'mascotas_adoptadas': reverse('mascotas_adoptadas-list', request=request, format=format),
    })


# Create your views here.

class MascotaAdopcion_List(generics.ListCreateAPIView):
    queryset = MascotaEnAdopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = MascotaEnAdopcion.objects.all()
        pj = self.request.query_params.get('puntaje_juego', None)
        if pj is not None:
            queryset = queryset.filter(puntaje_juego=pj)

        return queryset


class MascotaAdopcion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =MascotaEnAdopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize

class Mascotas(generics.ListCreateAPIView):
    queryset = Mascota.objects.all().order_by('nombre')
    serializer_class = Mascotaserialize

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Mascota.objects.all()
        tp = self.request.query_params.get('tipo_mascota', None)
        raza = self.request.query_params.get('raza', None)
        edad = self.request.query_params.get('edad', None)
        tipo = self.request.query_params.get('tipo', None)
        estado = self.request.query_params.get('estado', None)

        if tipo is not None:
            temp3=[]
            if tipo=="ADOP":
                temp=MascotaEnAdopcion.objects.all()
                temp2=Mascota.objects.all()
                for ob in temp:
                    for ob2 in temp2:
                        num=ob.id_mascota.id
                        print(ob.id_mascota.id)
                        if (num==ob2.id):
                            temp3.append(ob2.id)
                queryset=temp2.filter(id__in=temp3)
            if tipo == "P/E":
                temp = MascotaPerdidaEncontrada.objects.all()
                temp2 = Mascota.objects.all()
                for ob in temp:
                    for ob2 in temp2:
                        num = ob.id_mascota.id
                        print(ob.id_mascota.id)
                        if (num == ob2.id and (estado==ob.estado_mascota)):
                            temp3.append(ob2.id)
                queryset = temp2.filter(id__in=temp3)

        if tp is not None:
            if tp!="N":
                queryset = queryset.filter(tipo_mascota=tp)

        if edad is not None:
            if edad != "N":
             queryset = queryset.filter(edad_aproximada=edad)

        if raza is not None:
            if raza != "N":
              queryset = queryset.filter(razas=raza)

        return queryset

class MascotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = Mascotaserialize

class Razas(generics.ListCreateAPIView):
    queryset = Raza.objects.all().order_by('raza')
    serializer_class = Razaserialize

class RazaDetail(generics.RetrieveAPIView):
    queryset = Raza.objects.all()
    serializer_class = Razaserialize

class Mascotas_Perdida_Encontrada(generics.ListCreateAPIView):
    queryset = MascotaPerdidaEncontrada.objects.all()
    serializer_class = Mascota_Perdida_Encontrada_serialize

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = MascotaPerdidaEncontrada.objects.all()
        em  = self.request.query_params.get('estado_mascota', None)
        if em is not None:
            queryset = queryset.filter(estado_mascota=em)

        return queryset


class Mascotas_Perdida_Encontrada_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MascotaPerdidaEncontrada.objects.all()
    serializer_class = Mascota_Perdida_Encontrada_serialize

class Mascotas_Adoptadas(generics.ListCreateAPIView):
    queryset = MascotaAdoptada.objects.all()
    serializer_class = Mascota_Adoptada_serialize

class Mascotas_Adoptadas_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MascotaAdoptada.objects.all()
    serializer_class = Mascota_Adoptada_serialize
