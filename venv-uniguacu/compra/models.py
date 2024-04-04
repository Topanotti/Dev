from django.db import models
from requisicao.models import Requisicao
from fornecedor.models import Fornecedor
from item.models import Item

class Compra(models.Model):
    is_comprarequisicao = models.BooleanField(("Associação com Requisição"), default=False)
    requisicao = models.ForeignKey(Requisicao, on_delete=models.PROTECT, null=True, blank=True)
    is_compraitem = models.BooleanField(("Associação com Itens"), default=False)
    itens = models.ManyToManyField(Item)
    data = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=200)

    #def __str__(self):
        # Assuming 'date_field' is the field causing the issue
        #return f"{self.date_field.strftime('%d-%m-%Y')}"
