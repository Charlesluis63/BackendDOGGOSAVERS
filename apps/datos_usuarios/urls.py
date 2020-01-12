from django.conf.urls import url
from django.urls import path
from apps.datos_usuarios import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsuarioAPI
urlpatterns = [
    url("usuariosAPI/", UsuarioAPI.as_view()),
    path('persona/', views.Persona_List.as_view()),
    path('persona/<int:pk>/', views.Persona_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)