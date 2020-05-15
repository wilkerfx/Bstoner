from django import forms
from .models import Entrada, Saida


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada

        fields = [
        'descricao',
        'quantidade_entrada',
        'data'

        ]
        widgets = {
            'descriao': forms.Select(attrs={
                'class': 'regDropDown',
            }),

            'quantidade_entrada': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'data': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida

        fields = [
        'descricao',
        'quantidade_saida',
        'departamento',
        'data_saida'

]



