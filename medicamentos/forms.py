from os import name
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Medicamento


class medicamentoSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex = None, attrs = None):
        option: super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['name'] = value.instance.nome
        return super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
    
class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['Nome', 'RFID', 'Quantidade', 'Porta']
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'RFID': forms.TextInput(attrs={'class': 'form-control'}),
            'Quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'Porta': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(MedicamentoForm, self).__init__(*args, **kwargs)
        self.fields['Nome'].label = 'Nome'
        self.fields['RFID'].label = 'RFID'
        self.fields['Quantidade'].label = 'Quantidade'
        self.fields['Porta'].label = 'Porta'
    
    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('Nome')
        rfid = cleaned_data.get('RFID')
        quantidade = cleaned_data.get('Quantidade')
        porta = cleaned_data.get('Porta')
        
        if not nome:
            self.add_error('Nome', 'Campo obrigatório')
        if not rfid:
            self.add_error('RFID', 'Campo obrigatório')
        if not quantidade:
            self.add_error('Quantidade', 'Campo obrigatório')
        if not porta:
            self.add_error('Porta', 'Campo obrigatório')
        
        return cleaned_data