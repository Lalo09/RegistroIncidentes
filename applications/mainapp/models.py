from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class TipoIncidente(models.Model):
    tipo = models.CharField(max_length=60,verbose_name='Tipo')
    descripcion = models.TextField(verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Tipo de incidente'
        verbose_name_plural = 'Tipos de incidentes'        

    def __str__(self):
        return self.tipo

class Municipio(models.Model):
    nombre = models.CharField(max_length=60,verbose_name='nombre')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre

class Incidente(models.Model):
    folio = models.CharField(max_length=50,verbose_name='Folio')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(max_length=50,verbose_name='Hora')
    nombreAfectado = models.CharField(max_length=100,verbose_name='Nombre del afectado')
    numeroAfectado = models.CharField(max_length=20,verbose_name='Numero del afectado')
    descripcion = models.TextField(verbose_name='Descripcion de incidente')
    resulado = models.TextField(verbose_name='Resultado del incidente')
    nombreExtorsionador = models.CharField(max_length=60,verbose_name='Nombre del extorsionador',default='Desconocido')
    numeroExtorsionador = models.CharField(max_length=60,verbose_name='numero',default='Desconocido')
    cuentaExtorsionador = models.CharField(max_length=60,verbose_name='cuenta',default='Sin cuenta')
    deposito = models.FloatField(verbose_name='Cantidad depositado',default=0)
    usuario = models.ForeignKey(User,verbose_name='Atendio',on_delete=models.CASCADE,editable=False)
    tipoIncidente = models.ForeignKey(TipoIncidente,verbose_name='Tipo de incidente',on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,verbose_name='Municipio',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidentes'
        ordering = ['-id']

    def __str__(self):
        return str(self.id) + " | " + str(self.folio) + " | " + str(self.fecha) + " | " + str(self.hora) + " | " + self.nombreAfectado
        
