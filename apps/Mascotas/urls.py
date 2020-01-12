from django.conf.urls import url
from .views import MascotaAPI
urlpatterns = [
    url("mascotasAPI/", MascotaAPI.as_view())

]