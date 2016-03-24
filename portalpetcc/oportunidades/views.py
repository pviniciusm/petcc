from datetime import date
from django.shortcuts import render
from .models import Oportunidade

# Create your views here.
def oportunidades(request):
    hoje = date.today()
    ops = Oportunidade.objects.filter(data_limite__gte=hoje)
    return render(request, 'oportunidades/oportunidades.html', {'ops':ops})
