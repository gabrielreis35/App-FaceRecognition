from django.db import models
from medicos.models import Medico
from pacientes.models import Paciente
from medicamentos.models import Medicamento

class Prescricao(models.Model):
    Id = models.IntegerField(primary_key=True)
    IdMedico = models.ForeignKey(Medico, null=True, on_delete=models.SET_NULL)
    IdPaciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    IdMedicamento = models.ForeignKey(Medicamento, null=True, on_delete=models.SET_NULL)
    Data = models.DateTimeField()
    Quantidade = models.IntegerField()
    
    def __str__(self):
        return self.Id
    
    class Meta:
        db_table = 'Prescricao'