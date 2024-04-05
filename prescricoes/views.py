from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Prescricao
from django.shortcuts import render, redirect
from .forms import PrescricaoForm

def listPrescricoes(request):
    pesquisa = request.GET.get('pesquisa')
    if (pesquisa):
        prescricoes = Prescricao.objects.filter(Nome__icontains=request.GET.get('pesquisa'))
    else:
        prescricoes = Prescricao.objects.all().order_by('Nome')
        paginacao = Paginator(prescricoes, 10)
        pagina = request.GET.get('page')
        prescricoes = paginacao.get_page(pagina)
        
    contexto = {'prescricoes': prescricoes}
    return render(request, 'prescricao/listPrescricoes.html', contexto)

def detalhesPrescricao(request, id):
    prescricao = Prescricao.objects.get(Id=id)
    
    contexto = {'prescricao': prescricao}
    return render(request, 'prescricao/detalhesPrescricao.html', contexto)

def novaPrescricao(request):
    criarPrescricao = PrescricaoForm()
    if request.method == 'POST':
        criarPrescricao = PrescricaoForm(request.POST)
        if criarPrescricao.is_valid():
            criarPrescricao.save()
            return redirect('listPrescricoes')
        
    contexto = {'criarPrescricao': criarPrescricao}
    return render(request, 'prescricao/novaPrescricao.html', contexto)

def editarPrescricao(request, id):
    prescricao = Prescricao.objects.get(Id=id)
    editarPrescricao = PrescricaoForm(instance=prescricao)
    if request.method == 'POST':
        editarPrescricao = PrescricaoForm(request.POST, instance=prescricao)
        if editarPrescricao.is_valid():
            editarPrescricao.save()
            return redirect('listPrescricoes')
        
    contexto = {'editarPrescricao': editarPrescricao}
    return render(request, 'prescricao/editarPrescricao.html', contexto)
