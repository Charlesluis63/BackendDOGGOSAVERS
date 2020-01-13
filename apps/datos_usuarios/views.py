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


class Usuario_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Usuario.objects.all()
    serializer_class = Usuarioserialize

class Persona_List(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = Personaserialize


class Persona_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Persona.objects.all()
    serializer_class = Personaserialize