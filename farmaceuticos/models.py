from django.db import models

# Create your models here.
class Farmaceutico(models.Model):
    Id = models.IntegerField(primary_key=True)
    Cpf = models.CharField(max_length=11)
    Nome = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Senha = models.CharField(max_length=100)
    ReconhecimentoFacial = models.ImageField(upload_to='ReconhecimentoFacial')
    Rg = models.CharField(max_length=9)
    
    
    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = 'Farmaceutico'