from datetime import datetime
from django.db import models
from home.models import User


# Create your models here.
class Oportunidade(models.Model):
    usuario = models.ForeignKey(User)
    titulo = models.CharField(max_length=140, blank=False, null=False)
    texto = models.TextField(max_length=500, help_text="Descrição da oportunidade")
    bolsa = models.CharField(max_length=30, blank=True, help_text="Define o valor da bolsa, caso disponível")
    carga = models.IntegerField(blank=True, help_text="Define a carga horária semanal")
    local = models.CharField(max_length=50, help_text="Local onde será relizado o projeto/estágio")
    data_limite = models.DateField(blank=True, default=datetime.now())
    edital = models.URLField(blank=True)
