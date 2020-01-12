import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializer import Mascotaserialize
from .models import Mascota

# Create your views here.
class MascotaAPI(APIView):
    serializer = Mascotaserialize
    def get(self,request,format=None):
        lista = Mascota.objects.all()
        response = self.serializer(lista, many = True)
        return HttpResponse(json.dumps(response.data), content_type ='application/json')

