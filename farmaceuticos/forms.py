from django.forms import ModelForm
from .models import Farmaceutico

class FarmaceuticoForm(ModelForm):
    class Meta:
        model = Farmaceutico
        fields = ['Cpf', 'Nome', 'Email', 'Senha', 'ReconhecimentoFacial', 'Rg']