from django import forms
from resultado.models import DadosWeb

class NovoResultadoForm(forms.ModelForm):
    class Meta:
        model = DadosWeb
        fields = '__all__'
