from django.contrib import admin
from django.urls import path
from . import views

def testURL(self):
    print('=====Test URL from mainapp==========')

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name="logout"),
    path('incidentes/',views.ListadoIncidentes.as_view(),name='incidentes'),
    path('agregar_incidente/',views.AgregarIncidente.as_view(),name='agregar_incidente'),
    path('actualizar_incidente/<pk>',views.ActualizarIncidente.as_view(),name='actualizar_incidente'),
    path('eliminar_incidente/<pk>',views.EliminarIncidente.as_view(),name='eliminar_incidente'),
]

#Config admin panel
admin.site.site_header = "Gestion de incidentes"
admin.site.site_title = "Gestion de incidentes"
admin.site.index_title = "Administracion de folios"
