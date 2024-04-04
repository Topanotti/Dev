from django import forms
from .models import Requisicao

class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = ['numero', 'requerente', 'data', 'descricao']
        labels = {
            'numero': 'Número da Requisição', 
            'requerente': 'Requerente', 
            'data': 'Data',
            'descricao': 'Descrição'
        }
    widgets = {
       'numero': forms.NumberInput(attrs={'class':'form-control'}), 
        'requerente': forms.TextInput(attrs={'class':'form-control'}), 
        'data': forms.DateInput(format='%d-%m-%Y', attrs={'class':'form-control'}), 
        'descricao': forms.TextInput(attrs={'class':'form-control'}), 
    }    
