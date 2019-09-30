from django.contrib import admin

# Register your models here.
from .models import AlbumImagenes, RegionCampana, Estado, CaracteristicasAntena, Espectro, \
    PosicionAntena, Estadocamara, Estadoestacion

admin.site.register(AlbumImagenes)
admin.site.register(RegionCampana)
admin.site.register(Estado)
admin.site.register(CaracteristicasAntena)
admin.site.register(Espectro)
admin.site.register(PosicionAntena)
admin.site.register(Estadocamara)
admin.site.register(Estadoestacion)