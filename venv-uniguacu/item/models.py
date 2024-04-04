from django.db import models
from fornecedor.models import Fornecedor
from requisicao.models import Requisicao

class Item(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.IntegerField()
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    data_compra = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    requisicao = models.ForeignKey(Requisicao, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome