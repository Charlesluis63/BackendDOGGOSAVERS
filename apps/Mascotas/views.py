import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from .models import *

# Create your views here.
class MascotaAPI(APIView):
    serializer = Mascotaserialize
    def get(self,request,format=None):
        lista = Mascota.objects.all()
        response = self.serializer(lista, many = True)
        return HttpResponse(json.dumps(response.data), content_type ='application/json')

class MascotaAdopcion_List(generics.ListCreateAPIView):
    queryset = Mascota_En_Adopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize


class MascotaAdopcion_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Mascota_En_Adopcion.objects.all()
    serializer_class = Mascota_adopcion_serialize