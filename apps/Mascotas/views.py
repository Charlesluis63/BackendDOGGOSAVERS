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
    })


# Create your views here.

class MascotaAdopcion_List(generics.ListCreateAPIView):
    queryset = Mascota_En_Adopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize


class MascotaAdopcion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Mascota_En_Adopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize

class Mascotas(generics.ListCreateAPIView):
    queryset = Mascota.objects.all().order_by('nombre')
    serializer_class = Mascotaserialize

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
    queryset = Mascota_Perdida_Encontrada.objects.all()
    serializer_class = Mascota_Perdida_Encontrada_serialize

class Mascotas_Perdida_Encontrada_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota_Perdida_Encontrada.objects.all()
    serializer_class = Mascota_Perdida_Encontrada_serialize
