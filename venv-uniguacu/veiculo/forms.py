#from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit, Div, HTML
#from .models import Veiculo
#
#class VeiculoForm(forms.ModelForm):
#    class Meta:
#        model = Veiculo
#        fields = ['nome', 'placa', 'kilometragem', 'descricao', 'is_reservado', 'is_disponivel', 'motorista']
#        labels = {
#            'nome': 'Nome:',
#            'placa': 'Placa:',
#            'kilometragem': 'Kilometragem:',
#            'descricao': 'Descrição:',
#            'is_reservado': 'Reservado:',
#            'is_disponivel': 'Disponibilidade:',
#            'motorista': 'Motorista:'
#        }
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.form_method = 'post'
#        self.helper.layout = Layout(
#            Div(
#                *self.fields.keys(),  # Display all fields in the form
#                css_class='form-group'
#            ),
#            Div(
#                Submit('submit', 'Salvar', css_class='btn-primary'),  # Add submit button
#                HTML('<a href="{% url "index_veiculo" %}" class="btn btn-secondary">Cancelar</a>'),
#                css_class='col-10 offset-1 d-flex justify-content-between align-items-center'
#            ),
#        )
#
#    def crispy_helper(self):
#        return self.helper

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['nome', 'placa', 'kilometragem', 'descricao', 'is_reservado', 'is_disponivel', 'motorista']
        labels = {
            'nome': 'Nome:',
            'placa': 'Placa:',
            'kilometragem': 'Kilometragem:',
            'descricao': 'Descrição:',
            'is_reservado': 'Reservado:',
            'is_disponivel': 'Disponibilidade:',
            'motorista': 'Motorista:'
        }

    def __init__(self, *args, **kwargs):
        is_edit = kwargs.pop('is_edit', False)  # Check if it's in "edit" mode
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        buttons_layout = [
            Submit('submit', 'Salvar', css_class='btn-primary'),
            HTML('<a href="{% url "index_veiculo" %}" class="btn btn-secondary">Cancelar</a>')
        ]
        if is_edit:  # If it's in "edit" mode, include the "delete" button
            buttons_layout.append(HTML('<a href="{% url "delete_veiculo" veiculo.id %}" class="btn btn-danger">Deletar</a>'))
        self.helper.layout = Layout(
            Div(
                *self.fields.keys(),
                css_class='form-group'
            ),
            Div(
                *buttons_layout,
                css_class='col-10 offset-1 d-flex justify-content-between align-items-center'
            ),
        )

    def crispy_helper(self):
        return self.helper
