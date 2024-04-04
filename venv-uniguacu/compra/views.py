from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CompraForm
from compra.models import Compra
from requisicao.models import Requisicao
from fornecedor.models import Fornecedor




def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_compra')
    else:
        form = CompraForm()
    return render(request, 'compra/add_compra.html', {'form': form})

def index_compra(request):
    query = request.GET.get('query')
    compras = Compra.objects.all()
    if query:
        compras = compras.filter(data__icontains=query)
    return render(request, 'compra/index_compra.html', {'compras': compras, 'query': query})

def view_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    fornecedor = get_object_or_404(Fornecedor, pk=compra.fornecedor.id)
    print(fornecedor)
    requisicao = get_object_or_404(Requisicao, pk=compra.requisicao.id)
    return render(request, 'compra/view_compra.html', {'compra': compra, 'requisicao': requisicao, 'fornecedor' : fornecedor})

def edit_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('index_compra')
    else:
        form = CompraForm(instance=compra)

    return render(request, 'compra/edit_compra.html', {'form': form, 'compra': compra})

                                              


def delete_compra(request, id):
    if request.method == 'GET':
        compra = get_object_or_404(Compra, pk=id)
        compra.delete()
    return HttpResponseRedirect(reverse('index_compra'))

def pdf_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    return  render(request, 'compra/pdf_compra.html', {'compra': compra})