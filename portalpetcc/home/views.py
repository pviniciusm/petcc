from datetime import datetime, date

from django.contrib.auth.models import User
from django.shortcuts import render
from noticia.models import Noticia
from atividades.models import Atividade

# Create your views here.


def homepage(request):
    noticias = Noticia.objects.order_by('-data')[:5]
    atividades = Atividade.objects.filter(data_inicial__gte=date.today()).exclude(tipo="PESQ").order_by('-data_inicial').reverse()[:3]
    return render(request, 'home/homepage.html', {'noticias':noticias, 'atividades':atividades})


def sobre(request):
    usuarios = User.objects.all().exclude(id=1).exclude(situacao='T').exclude(situacao='C').order_by('?')
    tutor = User.objects.filter(situacao='T')
    colaboradores = User.objects.filter(situacao='C').order_by('?')
    return render(request, 'sobre/sobre.html', {'usuarios': usuarios, 'tutor': tutor, 'colaboradores': colaboradores})
