from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.IntegerField()
    endereco = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    email = models.EmailField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome