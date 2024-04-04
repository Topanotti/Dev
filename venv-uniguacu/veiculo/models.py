from django.db import models

class Veiculo(models.Model):
    
    nome = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    kilometragem = models.IntegerField()
    descricao = models.CharField(max_length=200)
    is_reservado = models.BooleanField()
    is_disponivel = models.BooleanField()
    motorista = models.CharField(max_length=50)
   