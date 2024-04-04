from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edit_mode = kwargs.pop('edit_mode', False)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                *self.visible_fields(),  # Display all visible fields in the form
                css_class='form-group'
            ),
            Div(
                Submit('submit', 'Salvar', css_class='btn-primary'),  # Add submit button
                HTML('<a href="{% url "index_veiculo" %}" class="btn btn-secondary">Cancelar</a>'),
                HTML('<a href="{% url "delete_veiculo" veiculo.id %}" onclick="return confirm(\'Tem certeza que deseja deletar esta veiculo?\')">Excluir</a>') if edit_mode else '',
                css_class='col-10 offset-1 d-flex justify-content-between align-items-center'
            ),
        )

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