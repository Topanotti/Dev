from django import forms
from .models import Item
from fornecedor.models import Fornecedor
from requisicao.models import Requisicao

class ItemForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    requisicao = forms.ModelChoiceField(queryset=Requisicao.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['nome', 'codigo', 'preco', 'quantidade', 'data_compra', 'fornecedor', 'requisicao', 'descricao']
        labels = {
            'nome': 'Nome do Item',
            'codigo': 'Código', 
            'preco': 'Preço', 
            'quantidade': 'Quantidade',
            'data_compra': 'Data da Compra',
            'fornecedor': 'Fornecedor',
            'requisicao': 'Requisição',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.NumberInput(attrs={'class':'form-control'}), 
            'preco': forms.NumberInput(attrs={'class':'form-control'}), 
            'quantidade': forms.NumberInput(attrs={'class':'form-control'}), 
            'data_compra': forms.DateInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
        }
