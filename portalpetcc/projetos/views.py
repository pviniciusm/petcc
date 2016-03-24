from django.shortcuts import render
from atividades.models import Atividade


# Create your views here.
def projetos(request):
    return render(request, 'projetos/projetos.html', {})


def ensino(request):
    prj = Atividade.objects.filter(tipo='MN') | Atividade.objects.filter(tipo='PEC') | \
          Atividade.objects.filter(tipo='SEM') | Atividade.objects.filter(tipo='TA') | \
          Atividade.objects.filter(tipo='OU')
    return render(request, 'projetos/ensino.html', {'prj': prj})


def pesquisa(request):
    prj = Atividade.objects.filter(tipo='PESQ')
    return render(request, 'projetos/pesquisa.html', {'prj': prj})


def extensao(request):
    Atividade.objects.filter(tipo='EX')
    return render(request, 'projetos/projetos.html', {'prj': prj})
