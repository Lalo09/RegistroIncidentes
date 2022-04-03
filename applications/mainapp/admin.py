from django.contrib import admin
from .models import Incidente,Municipio,TipoIncidente
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(Municipio)
admin.site.register(TipoIncidente)

class IncidenteResources(resources.ModelResource):
    fields = (
        'folio',
        'fecha',
        'hora',
        'nombreAfectado',
        'tipoIncidente',
        'usuario'
    )

    class Meta:
        model = Incidente

class IncidenteAdmin(ImportExportModelAdmin):
    resource_class = IncidenteResources
    list_display = (
        'folio',
        'fecha',
        'hora',
        'nombreAfectado',
        'tipoIncidente',
        'usuario'
    )
    readonly_fields = ('usuario',)
    search_fields = ('first_name',)
    list_filter = ('fecha','tipoIncidente',)

    """def save_model(self,request,obj,form, change):
        if not obj.usuario_id:
            obj.usuario_id = request.user.id

        obj.save()"""
        

admin.site.register(Incidente,IncidenteAdmin)