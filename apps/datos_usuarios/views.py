import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import Usuarioserialize,Persona_serialize
from .models import Persona,Usuario

@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'persona': reverse('persona-list', request=request, format=format),
        'usuario': reverse('usuario-list', request=request, format=format),
    })

# Create your views here.

class Usuario_List(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = Persona_serialize


class Usuario_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Persona.objects.all()
    serializer_class = Persona_serialize

class Persona_List(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = Persona_serialize


class Persona_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Persona.objects.all()
    serializer_class = Persona_serialize