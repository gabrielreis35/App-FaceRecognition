from django.db import models

class Medicamento(models.Model):
    Id = models.IntegerField(primary_key=True)
    Nome = models.CharField(max_length=100)
    RFID = models.CharField(max_length=100)
    Quantidade = models.IntegerField()
    DataRetirada = models.DateTimeField()
    
    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = 'Medicamento'