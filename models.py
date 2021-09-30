from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Veiculo(models.Model):
    detalhamento = models.CharField(max_length = 300)
    fabricanteVeiculo = models.CharField(max_length = 100)
    modeloVeiculo = models.CharField(max_length = 100)
    anoVeiculo = models.CharField(max_length = 4)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length = 150)
    telefone = models.CharField(max_length = 15)

class Mecanico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length = 150)
    telefone = models.CharField(max_length = 15)

class Consultoria(models.Model):
    data = models.DateTimeField('data')
    local = models.CharField(max_length = 300)
    temConsultor = models.CharField(max_length = 1)
    plano = models.CharField(max_length = 20)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, default=1)
    cliente = models.IntegerField()
    mecanico = models.IntegerField()