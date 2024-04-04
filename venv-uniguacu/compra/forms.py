# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['is_comprarequisicao', 'requisicao', 'is_compraitem', 'itens', 'data', 'fornecedor', 'descricao']
        labels = {
            'is_comprarequisicao': 'Associação com Requisição',
            'requisicao': 'Requisição',
            'is_compraitem': 'Associação com Itens',
            'itens': 'Itens',
            'data': 'Data',
            'fornecedor': 'Fornecedor',
            'descricao': 'Descrição'
        }
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))
