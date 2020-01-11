from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Raza)
admin.site.register(Mascota_Adoptada)
admin.site.register(Mascota_En_Adopcion)
admin.site.register(Mascota_Perdida_Encontrada)



