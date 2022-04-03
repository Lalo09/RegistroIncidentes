from django import forms
from .models import Incidente


class AgreagarIncidenteForm(forms.ModelForm):

    class Meta:
        model = Incidente
        fields = ('folio',
        'fecha',
        'hora',
        'nombreAfectado',
        'numeroAfectado',
        'descripcion',
        'resulado',
        'nombreExtorsionador',
        'numeroExtorsionador',
        'cuentaExtorsionador',
        'deposito',
        'tipoIncidente',
        'municipio')
        widgets={
            'folio':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'hora':forms.TimeInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'time'}),
            'nombreAfectado':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'numeroAfectado':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control'
                }
            ),
            'resulado':forms.Textarea(
                attrs = {
                    'class':'form-control'
                }
            ),
            'nombreExtorsionador':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'numeroExtorsionador':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'cuentaExtorsionador':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'deposito':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }