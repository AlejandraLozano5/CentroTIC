from django import forms 
from .models import Integrantes, Semillero

class IntegrantesForm(forms.ModelForm):
    class Meta:
        model = Integrantes
        fields = ('nombre','telefono', 'semillero')

class SemilleroForm(forms.ModelForm):
    class Meta:
        model = Semillero
        fields = ('responsable','telefono', 'kit', 'colegio')

class ConsultaIntegrantesForm(forms.ModelForm):
    
    class Meta:
        model = Integrantes
        fields = ("semillero",)


class ConsultaSemilleroForm(forms.ModelForm):
    class Meta:
        model = Semillero
        fields = ('colegio',)