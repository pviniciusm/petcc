from datetime import datetime, date
from django.shortcuts import render
from noticia.models import Noticia
from atividades.models import Atividade

# Create your views here.


def homepage(request):
    noticias = Noticia.objects.order_by('-data')[:5]
    atividades = Atividade.objects.filter(data_inicial__gte=date.today()).order_by('-data_inicial').reverse()[:3]
    return render(request, 'home/homepage.html', {'noticias':noticias, 'atividades':atividades})