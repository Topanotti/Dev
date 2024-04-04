from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'endereco', 'contato', 'email', 'descricao']
        labels = {
            'nome': 'Nome do Fornecedor', 
            'cnpj': 'CNPJ', 
            'endereco': 'Endereço',
            'contato': 'Contato',
            'email': 'email',
            'descricao': 'Descrição'
        }
    widgets = {
       'nome': forms.TextInput(attrs={'class':'form-control'}), 
        'cnpj': forms.NumberInput(attrs={'class':'form-control'}), 
        'endereco': forms.TextInput(attrs={'class':'form-control'}),
        'contato': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'}), 
        'descricao': forms.TextInput(attrs={'class':'form-control'}), 
    }    
