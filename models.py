from django.db import models

# Create your models here.
class Consultoria(models.Model):
    data = models.DateTimeField('data')
    local = models.CharField(max_length = 300)
    detalhamento = models.CharField(max_length = 300)
    fabricanteVeiculo = models.CharField(max_length = 100)
    modeloVeiculo = models.CharField(max_length = 100)
    anoVeiculo = models.CharField(max_length = 4)
    temConsultor = models.CharField(max_length = 1)
    plano = models.CharField(max_length = 20)