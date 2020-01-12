from django.conf.urls import url
from django.urls import path, include
from apps.Mascotas import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MascotaAPI


urlpatterns = [
    url("mascotasAPI/", MascotaAPI.as_view()),
    path('mascotasadopcion/', views.MascotaAdopcion_List.as_view(), name='mascotasadopcion-list'),
    path('mascotasadopcion/<int:pk>/', views.MascotaAdopcion_Detail.as_view(), name='mascotasadopcion-detail'),
    path('mascotas/', views.MascotaAPI.as_view(), name='mascotas-list'),
    path('mascotas/<int:pk>/', views.MascotaDetail.as_view(), name='mascota-detail'),
    path('raza/', views.Razas.as_view(), name='razas-list'), # new
    path('razas/<int:pk>/', views.RazaDetail.as_view(), name='razas-detail'),
    path('mascota_perdida_encontrada/', views.Mascotas_Perdida_Encontrada.as_view(), name='mascota_perdida_encontrada-list'), # new
    path('mascota_perdida_encontrada/<int:pk>/', views.Mascotas_Perdida_Encontrada_Detail.as_view(), name='mascota_perdida_encontrada-detail'),
    path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)