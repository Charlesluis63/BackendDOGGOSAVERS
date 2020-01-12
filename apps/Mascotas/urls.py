from django.conf.urls import url
from django.urls import path
from apps.Mascotas import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MascotaAPI
urlpatterns = [
    url('mascotasAPI/', MascotaAPI.as_view()),
    path('mascotasadopcion/', views.MascotaAdopcion_List.as_view()),
    path('mascotasadopcion/<int:pk>/', views.MascotaAdopcion_Detail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)