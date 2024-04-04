from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from item.forms import ItemForm
from .models import Item
from django.db.models import Q
from fornecedor.models import Fornecedor
from requisicao.models import Requisicao

# Create your views here.
def index_item(request):
    query = request.GET.get('query')
    items = Item.objects.all()
    if query:
        items = items.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
    return render(request, 'item/index_item.html', {'items': items, 'query': query})

def add_item(request):
    fornecedores = Fornecedor.objects.all()
    requisicoes = Requisicao.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            new_nome = form.cleaned_data['nome']
            new_codigo = form.cleaned_data['codigo']
            new_preco = form.cleaned_data['preco']
            new_quantidade = form.cleaned_data['quantidade']
            new_data_compra = form.cleaned_data['data_compra']
            new_fornecedor = form.cleaned_data['fornecedor']
            new_requisicao = form.cleaned_data['requisicao']
            new_descricao = form.cleaned_data['descricao']
            
            new_item = Item(
                nome = new_nome,
                codigo = new_codigo,
                preco = new_preco,
                quantidade = new_quantidade,
                data_compra = new_data_compra,
                fornecedor = new_fornecedor,
                requisicao = new_requisicao,
                descricao = new_descricao
            )
        new_item.save()
        return render(request, 'item/add_item.html', {
            'fornecedores': fornecedores,
            'requisicoes': requisicoes,
            'form': ItemForm(),
            'success': True
        })
    else:
        form = ItemForm()
    return render(request, 'item/add_item.html', {
        'form': ItemForm(),
        'fornecedores': fornecedores,
        'requisicoes': requisicoes,
    } )   

def view_item(request, id):
    item = Item.objects.get(pk=id)
    fornecedor_nome = item.fornecedor.nome
    requisicao_numero = item.requisicao.numero
    return render(request, 'item/view_item.html', {'item': item, 'fornecedor_nome': fornecedor_nome, 'requisicao_numero': requisicao_numero})


def edit_item(request, id):
    fornecedores = Fornecedor.objects.all()
    requisicoes = Requisicao.objects.all()
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'item/edit_item.html', {
                'fornecedores': fornecedores,
                'requisicoes': requisicoes,
                'form': ItemForm(),
                'item': item,  
                'success': True
            })
    else:
        form = ItemForm(instance=item)
    return render(request, 'item/edit_item.html', {
        'fornecedores': fornecedores,
        'requisicoes': requisicoes,
        'form': form,
        'item': item,
    })

def delete_item(request, id):
    print('Deletando Item...')
    if request.method == 'GET':
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('index_item'))