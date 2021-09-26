from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Consultoria

# Create your views here.

def home(request):
    return render(request, 'avaliauto/home.html')

def index(request):
    consultorias = Consultoria.objects.order_by('data')

    context = {
        'consultorias': consultorias
    }
    return render(request, 'avaliauto/index.html', context)


def show(request):
    consultorias = Consultoria.objects.filter(temConsultor='N')

    context = {
        'consultorias': consultorias
    }
    return render(request, 'avaliauto/listar.html', context)



def inserir(request):
    dt = request.POST['data']
    loc = request.POST['local']
    det = request.POST['detalhamento']
    fab = request.POST['fabricanteVeiculo']
    plan = 'Plus'
    model = request.POST['modeloVeiculo']
    ano = request.POST['anoVeiculo']
    consul = 'N'

    consultoria = Consultoria(data = dt, local = loc, detalhamento = det, fabricanteVeiculo = fab, plano = plan, modeloVeiculo = model, anoVeiculo = ano, temConsultor = consul)
    consultoria.save()

    return HttpResponseRedirect("/avaliauto/")


def aceitarConsultoria(request, id):
    consultoria = get_object_or_404(Consultoria, pk=id)

    dt = consultoria.data
    loc = consultoria.local
    det = consultoria.detalhamento
    fab = consultoria.fabricanteVeiculo
    plan = consultoria.plano
    model = consultoria.modeloVeiculo
    ano = consultoria.anoVeiculo

    consultoria = Consultoria(id = consultoria.id, data = dt, local = loc, detalhamento = det, fabricanteVeiculo = fab, plano = plan, modeloVeiculo = model, anoVeiculo = ano, temConsultor = "Y")

    consultoria.save()
    return HttpResponseRedirect("/avaliauto/minhasConsultorias")


def minhas_consultorias(request):
    consultorias = Consultoria.objects.filter(temConsultor='Y')

    context = {
        'consultorias': consultorias
    }
    return render(request, 'avaliauto/minhasConsultorias.html', context)













