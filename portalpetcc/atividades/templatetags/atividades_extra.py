from datetime import date
from django import template
from atividades.models import *

register = template.Library()


@register.filter(name='minicurso_finalizado')
def minicurso_finalizado(value):
    hoje = date.today()
    if hoje > value:
        return True
    else:
        return False


tipos={
    'MN':'Minicurso',
    'PEC': 'Palestra',
    'SEM': 'Seminário',
    'TA': 'Tópico de Apoio',
    'PESQ': 'Pesquisa',
    'EX': 'Extensão',
    'OU': 'Projeto'
}

tipos_sit = {
    'B': 'Bolsista',
    'C': 'Colaborador',
    'N': 'Nao-bolsista',
    'T': 'Tutor'
}


@register.filter(name='tipomin')
def tipomin(value):
    return tipos[value]


@register.filter(name='tiposit')
def tiposit(value):
    return tipos_sit[value]

