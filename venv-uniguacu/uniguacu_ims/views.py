from fornecedor.models import Fornecedor
from item.models import Item
from requisicao.models import Requisicao
from django.shortcuts import render
from django.db.models import Q

def dashboard(request):
    return render(request, 'dashboard.html')

def search(request):
    query = request.GET.get('query')
    if query:
        fornecedores = Fornecedor.objects.filter(nome__icontains=query)
        items = Item.objects.filter(nome__icontains=query)
        requisicoes = Requisicao.objects.filter(Q(numero__icontains=query) | Q(descricao__icontains=query))
    else:
        fornecedores = Fornecedor.objects.none()
        items = Item.objects.none()
        requisicoes = Requisicao.objects.none()
    return render(request, 'search.html', {'fornecedores': fornecedores, 'items': items, 'requisicoes': requisicoes, 'query': query})
