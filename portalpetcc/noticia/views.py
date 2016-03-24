from django.shortcuts import render
from django.shortcuts import get_object_or_404
from noticia.models import *

# Create your views here.
def noticias(request, slug):
    notic = get_object_or_404(Noticia, slug=slug)
    notic.visualizacoes += 1
    notic.save()
    news_pop = Noticia.objects.all().order_by('visualizacoes').reverse()[:5]
    news_ult = Noticia.objects.all().order_by('data').reverse()[:5]
    return render(request, 'noticia/noticia.html', {'noticia' : notic, 'newspop':news_pop, 'newsult':news_ult})

def ultimasnoticias(request):
    news = Noticia.objects.all().order_by('data').reverse()
    news_pop = Noticia.objects.all().order_by('visualizacoes').reverse()[:5]
    return render(request, 'noticia/noticias.html', {'noticias' : news, 'newspop':news_pop})