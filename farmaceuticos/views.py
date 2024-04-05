from django.shortcuts import render
from django.http import HttpResponse
from .models import Farmaceutico
from .forms import FarmaceuticoForm
from login.models import UserProfile

def listFarmaceuticos(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        data = UserProfile.objects.filter(TipoUsuario="farmaceutico") #Farmaceutico.objects.filter(Nome__icontains=pesquisa)  
    else:    
        data = Farmaceutico.objects.all()
    context = {'farmaceuticos': data}
    
    return render(request, 'farmaceuticos/ListFarmaceuticos.html', context)


def createFarmaceutico(request):
    farmaceutico = FarmaceuticoForm()
    if request.method == 'POST':
        farmaceutico = FarmaceuticoForm(request.POST)
        if farmaceutico.is_valid():
            farmaceutico.save()
            return HttpResponse('Farmaceutico criado com sucesso!')
    else:
        farmaceutico = FarmaceuticoForm()
    context = {'form': farmaceutico}
    
    return render(request, 'farmaceuticos/CreateFarmaceutico.html', context)

def updateFarmaceutico(request, id):
    farmaceutico = Farmaceutico.objects.get(id=id)
    form = FarmaceuticoForm(instance=farmaceutico)
    if request.method == 'POST':
        form = FarmaceuticoForm(request.POST, instance=farmaceutico)
        if form.is_valid():
            form.save()
            return HttpResponse('Farmaceutico atualizado com sucesso!')
    context = {'form': form}
    
    return render(request, 'farmaceuticos/UpdateFarmaceutico.html', context)

def deleteFarmaceutico(request, id):
    farmaceutico = Farmaceutico.objects.get(id=id)
    if request.method == 'DELETE':
        farmaceutico.delete()
    context = {'item': farmaceutico}
    
    return HttpResponse(request, 'farmaceuticos/ListFarmaceuticos.html', context)