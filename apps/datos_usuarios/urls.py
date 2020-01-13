from django.conf.urls import url
from django.urls import path
from apps.datos_usuarios import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('usuario/', views.Usuario_List.as_view()),
    path('usuario/<int:pk>/', views.Usuario_Detail.as_view()),
    path('persona/', views.Persona_List.as_view()),
    path('persona/<int:pk>/', views.Persona_Detail.as_view()),
    path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)