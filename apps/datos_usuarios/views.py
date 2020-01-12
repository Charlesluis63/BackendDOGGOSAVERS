import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import Usuarioserialize,Persona_serialize
from .models import Persona,Usuario



# Create your views here.
class UsuarioAPI(APIView):
    serializer = Usuarioserialize
    def get(self,request,format=None):
        lista = Usuario.objects.all()
        response = self.serializer(lista, many = True)
        return HttpResponse(json.dumps(response.data), content_type ='application/json')


class Persona_List(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = Persona_serialize


class Persona_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Persona.objects.all()
    serializer_class = Persona_serialize