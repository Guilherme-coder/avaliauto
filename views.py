from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Cliente, Mecanico, Veiculo
from django.urls import reverse

from .models import Consultoria

# Create your views here.
def auth_in(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(
        request,
        username,
        password
    )
    if user is not None:
        login(request)
        return user(request)
    return render(request, 'avaliauto/login.html')

def auth_out(request):
    logout(request)

def auth_up_client(request):
    nome = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    senha = request.POST['senha']
    nome = request.POST['name']
    user = User.objects.create_user(
        first_name = nome,
        email = email,
        username = username,
        password = senha
    )
    user.save()

    nome_cliente = request.POST['nome_cliente']
    telefone = request.POST['telefone']
    cliente = Cliente.objects.create(
        user = user.id,
        nome = nome_cliente,
        telefone = telefone
    )
    cliente.save()
    return render(request, 'avaliauto/home.html')


def auth_up_mecanico(request):
    nome = request.POST['nome']
    email = request.POST['email']
    username = request.POST['username']
    senha = request.POST['senha']
    user = User.objects.create_user(
        first_name = nome,
        email = email,
        username = username,
        password = senha
    )
    user.save()

    nome_mecanico = request.POST['nome_mecanico']
    telefone = request.POST['telefone']
    mecanico = Mecanico.objects.create(
        user = user.id,
        nome = nome_mecanico,
        telefone = telefone
    )
    mecanico.save()
    return render(request, 'avaliauto/home.html')


def home(request):
    return render(request, 'avaliauto/home.html')

def index(request):
    consultorias = Consultoria.objects.order_by('data')

    context = {
        'consultorias': consultorias
    }
    return render(request, 'avaliauto/index.html', context)


def show(request):
    consultorias = Consultoria.objects.filter(mecanico=1)

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

    veiculo = Veiculo(
        detalhamento = det,
        fabricanteVeiculo = fab,
        modeloVeiculo = model,
        anoVeiculo = ano
    )
    veiculo.save()

    consultoria = Consultoria(
        data = dt,
        local = loc,
        plano = plan,
        veiculo = veiculo,
        #cliente = request.user.id,
        cliente = 1,
        mecanico = 1
    )
    consultoria.save()

    return HttpResponseRedirect("/avaliauto/")


def aceitarConsultoria(request, id):
    consultoria = get_object_or_404(Consultoria, pk=id)

    dt = consultoria.data
    loc = consultoria.local
    plan = consultoria.plano

    consultoria = Consultoria(
        id = consultoria.id,
        data = dt,
        local = loc,
        plano = plan,
        veiculo = consultoria.veiculo,
        cliente = consultoria.cliente,
        #mecanico = request.user.id,
        mecanico = 2
    )

    consultoria.save()
    return HttpResponseRedirect("/avaliauto/minhasConsultorias")


def minhas_consultorias(request):
    consultorias = Consultoria.objects.exclude(mecanico = 1)

    context = {
        'consultorias': consultorias
    }
    return render(request, 'avaliauto/minhasConsultorias.html', context)













