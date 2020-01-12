from django.conf.urls import url
from .views import PersonaAPI,UsuarioAPI
urlpatterns = [
    url("personasAPI/", PersonaAPI.as_view()),
    url("usuariosAPI/", UsuarioAPI.as_view())

]