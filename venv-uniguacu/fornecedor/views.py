from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from fornecedor.forms import FornecedorForm
from .models import Fornecedor

# Create your views here.
def index_fornecedor(request):
    query = request.GET.get('query')
    fornecedores = Fornecedor.objects.all()
    if query:
        fornecedores = fornecedores.filter(Q(nome__icontains=query) | Q(descricao__icontains=query) | Q(cnpj__icontains=str(query)))
    return render(request, 'fornecedor/index_fornecedor.html', {'fornecedores': fornecedores, 'query': query})

def add_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            new_nome = form.cleaned_data['nome']
            new_cnpj = form.cleaned_data['cnpj']
            new_endereco = form.cleaned_data['endereco']
            new_contato = form.cleaned_data['contato']
            new_email = form.cleaned_data['email']
            new_descricao = form.cleaned_data['descricao']
            
            new_fornecedor = Fornecedor(
                nome = new_nome,
                cnpj = new_cnpj,
                endereco = new_endereco,
                contato = new_contato,
                email = new_email,
                descricao = new_descricao
            )
        new_fornecedor.save()
        return render(request, 'fornecedor/add_fornecedor.html', {
            'form': FornecedorForm(),
            'success': True
        })
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor/add_fornecedor.html', {
        'form': FornecedorForm()
    } )    

def view_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    return render(request, 'fornecedor/view_fornecedor.html', {'fornecedor':fornecedor})
    
def edit_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return render(request, 'fornecedor/edit_fornecedor.html', {
                'form': form,
                'success': True
            })
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedor/edit_fornecedor.html', {
        'form': form,
        'fornecedor': fornecedor,
    })

def delete_fornecedor(request, id):
    print('Deletando Fornecedor...')
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.get(pk=id)
        fornecedor.delete()
    return HttpResponseRedirect(reverse('index_fornecedor'))
    