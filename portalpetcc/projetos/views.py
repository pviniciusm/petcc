from django.shortcuts import render, get_object_or_404
from atividades.models import Atividade


# Create your views here.
def projetos(request):
    pesq = Atividade.objects.filter(tipo='PESQ')[:4]
    ext = Atividade.objects.filter(tipo='EX')[:4]
    return render(request, 'projetos/projetos.html', {'pesq': pesq, 'ext': ext})


def ensino(request):
    prj = Atividade.objects.filter(tipo='MN') | Atividade.objects.filter(tipo='PEC') | \
          Atividade.objects.filter(tipo='SEM') | Atividade.objects.filter(tipo='TA') | \
          Atividade.objects.filter(tipo='OU')
    return render(request, 'projetos/ensino.html', {'prj': prj})


def pesquisa(request):
    prj = Atividade.objects.filter(tipo='PESQ')
    return render(request, 'projetos/pesquisa.html', {'prj': prj})


def extensao(request):
    prj = Atividade.objects.filter(tipo='EX')
    return render(request, 'projetos/extensao.html', {'prj': prj})


def projeto(request, id):
    prj = get_object_or_404(Atividade, id=id)
    return render(request, 'projetos/projeto.html', {'projeto': prj})


def atividades(request, slug):
    prj = get_object_or_404(Atividade, slug=slug)
    return render(request, 'projetos/projeto.html', {'projeto': prj})
