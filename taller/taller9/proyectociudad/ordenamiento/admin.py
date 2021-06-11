from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia')
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)