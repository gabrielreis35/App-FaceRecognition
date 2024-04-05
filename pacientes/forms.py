from os import name
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Paciente


class medicamentoSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex = None, attrs = None):
        option: super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['name'] = value.instance.nome
        return super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'Cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Rg': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['Nome'].label = 'Nome'
        self.fields['Cpf'].label = 'Cpf'
        self.fields['Email'].label = 'Email'
        self.fields['Rg'].label = 'Rg'
        
    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('Cpf')
        rg = cleaned_data.get('Rg')
        email = cleaned_data.get('Email')
        
        if not cpf and not rg and not email:
            raise forms.ValidationError('Informe ao menos um campo para salvar o paciente')
        
        return cleaned_data
    
    def save(self, commit=True):
        paciente = super(PacienteForm, self).save(commit=False)
        if commit:
            paciente.save()
        return paciente