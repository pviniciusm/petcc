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


@register.filter(name='certificado_tipo')
def certificado_tipo(value):
    if value == "OU":
        return 'evento intitulado'

    substr = "intitulado"
    prestr = "do"
    if value == "MN":
        substr = "sobre"

    if value == "PEC":
        prestr = "da"
        substr = "intitulada"
        str = "PEC"

    else:
        str = tipos[value]
    return "%s %s %s" % (prestr, str, substr)


@register.filter(name='carga')
def carga(value, value2):
    if value == 0:
        return value2
    return value


@register.filter(name='responsavel')
def responsavel(value):
    if value.startswith("PET"):
        return True

    return False


@register.filter(name='aluno')
def aluno(value):
    if value:
        return ", matrícula %s," % value

    else:
        return ""
