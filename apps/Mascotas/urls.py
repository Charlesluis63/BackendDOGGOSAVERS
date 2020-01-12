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
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)