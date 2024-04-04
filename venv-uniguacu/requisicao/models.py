from django.db import models

# Create your models here.
class Requisicao(models.Model):
    numero = models.IntegerField()
    requerente = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.CharField(max_length=300)

    #def __str__(self):
    #    return str(self.numero, self.requerente, self.data)