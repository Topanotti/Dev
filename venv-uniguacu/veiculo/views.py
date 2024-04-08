from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from veiculo.models import Veiculo
from veiculo.forms import VeiculoForm

def index_veiculo(request):
    query = request.GET.get('query')
    veiculos = Veiculo.objects.all()
    if query:
        veiculos = veiculos.filter(data__icontains=query)
    return render(request, 'veiculo/index_veiculo.html', {'veiculos': veiculos, 'query': query})

def add_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_veiculo')
    else:
        form = VeiculoForm()
    return render(request, 'veiculo/add_veiculo.html', {'form': form})

def edit_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('index_veiculo')
    else:
        form = VeiculoForm(instance=veiculo, is_edit=True)  # Pass is_edit=True for edit mode
    return render(request, 'veiculo/edit_veiculo.html', {'form': form, 'veiculo': veiculo})

def view_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    return render(request, 'veiculo/view_veiculo.html', {'veiculo': veiculo})

def delete_veiculo(request):
    print('Deletando Veículo...')
    if request.method == 'GET':
        veiculo = Veiculo.objects.get(pk=id)
        veiculo.delete()
    return HttpResponseRedirect(reverse('index_veiculo'))        

def pdf_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    return 



#def edit_veiculo(request, id):
#    veiculo = get_object_or_404(Veiculo, pk=id)
#    if request.method == 'POST':
#        form = VeiculoForm(request.POST, instance=veiculo, edit_mode=True)
#        if form.is_valid():
#            form.save()
#            return redirect('index_veiculo')
#    else:
#        form = VeiculoForm(instance=veiculo)
#    context = {
#        'form': form,  # Make sure the form is passed to the template context
#        'veiculo': veiculo,
#    }
#    return render(request, 'veiculo/edit_veiculo.html', context)

def view_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    return render(request, 'veiculo/view_veiculo.html', {'veiculo': veiculo})

def delete_veiculo(request):
    return render(request, 'veiculo/index_veiculo.html')

