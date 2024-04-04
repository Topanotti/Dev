from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.urls import reverse
from django.db.models import Q
from requisicao.models import Requisicao
from requisicao.forms import RequisicaoForm
from reportlab.lib.pagesizes import A4


def index_requisicao(request):
    query = request.GET.get('query')
    requisicoes = Requisicao.objects.all()
    if query:
        requisicoes = requisicoes.filter(Q(numero__icontains=query) | Q(requerinte__icontains=query) | Q(data__icontains=str(query)))
    return render(request, 'requisicao/index_requisicao.html', {'requisicoes': requisicoes, 'query': query})

def view_requisicao(request, id):
    requisicao = Requisicao.objects.get(pk=id)
    return render(request, 'requisicao/view_requisicao.html', {'requisicao':requisicao})

def add_requisicao(request):
    if request.method == 'POST':
        form = RequisicaoForm(request.POST)
        if form.is_valid():
            new_numero = form.cleaned_data['numero']
            new_requerente = form.cleaned_data['requerente']
            new_data = form.cleaned_data['data']
            new_descricao = form.cleaned_data['descricao']
            
            new_requisicao = Requisicao(
                numero = new_numero,
                requerente = new_requerente,
                data = new_data,
                descricao = new_descricao
            )
        new_requisicao.save()
        return render(request, 'requisicao/add_requisicao.html', {
            'form': RequisicaoForm(),
            'success': True
        })
    else:
        form = RequisicaoForm()
    return render(request, 'requisicao/add_requisicao.html', {
        'form': RequisicaoForm()
    } )    
    

def edit_requisicao(request, id):
    requisicao = Requisicao.objects.get(pk=id)
    if request.method == 'POST':
        form = RequisicaoForm(request.POST, instance=requisicao)
        if form.is_valid():
            form.save()
            return render(request, 'requisicao/edit_requisicao.html', {
                'form': form,
                'success': True
            })
    else:
        form = RequisicaoForm(instance=requisicao)
    return render(request, 'requisicao/edit_requisicao.html', {
        'form': form,
        'requisicao': requisicao,
    })

def delete_requisicao(request):
    print('Deletando Requisição...')
    if request.method == 'GET':
        requisicao = Requisicao.objects.get(pk=id)
        requisicao.delete()
    return HttpResponseRedirect(reverse('index_requisicao'))

def pdf_requisicao(request, id):
    # Fetch the requisicao object from the database
    requisicao = Requisicao.objects.get(pk=id)

    # Render HTML template with requisicao data
    html = render_to_string('requisicao/pdf_requisicao.html', {'requisicao': requisicao})

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="requisicao_{requisicao.numero}.pdf"'

    # Create PDF
    pdf = SimpleDocTemplate(response, pagesize=A4)
    pisa.CreatePDF(html, dest=pdf)

    return response