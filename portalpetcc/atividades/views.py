import json

from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import *
from home.models import User
from django.db.models import Count


# Create your views here.
@csrf_protect
def minicursos(request):
    ano_corrente = datetime.now().year
    minic = Atividade.objects.filter(tipo='MN', data_inicial__year=ano_corrente)
    minic_ant = Atividade.objects.filter(tipo='MN').exclude(data_inicial__year=ano_corrente).order_by('data_inicial').reverse()[:2]
    return render(request, 'atividade/minicursos.html', {'minic' : minic, 'minic_ant':minic_ant})

cursos = {
    "cc" : "Ciência da Computação",
    "si" : "Sistemas de Informação",
    "sint" : "Sistemas para Internet",
    "rc" : "Redes de Computadores",
    "ec" : "Engenharia de Computação",
    "ou" : "Outro",
}

meses = {
    "1":"Janeiro",
    "2":"Fevereiro",
    "3":"Março",
    "4":"Abril",
    "5":"Maio",
    "6":"Junho",
    "7":"Julho",
    "8":"Agosto",
    "9":"Setembro",
    "10":"Outubro",
    "11":"Novembro",
    "12":"Dezembro",
}


@csrf_protect
def createparticipacao(request):
    if request.method == 'POST':
        response_data = {}

        matricula = int(request.POST.get('matricula'))
        minic = int(request.POST.get('minicurso'))

        try:
            usuario = Aluno.objects.get(matricula=matricula)
            if not usuario.participante:
                usuario.participante = True
            if not usuario.curso == cursos[request.POST.get('curso')]:
                usuario.curso = request.POST.get('curso')

            if not request.POST.get('nome') == "" and not request.POST.get('sobrenome') == "":
                usuario.first_name = request.POST.get('nome')
                usuario.last_name = request.POST.get('sobrenome')

        except:
            curso = request.POST.get('curso')
            usuario = Aluno(matricula=matricula, username=matricula, first_name=request.POST.get('nome'),
                            last_name=request.POST.get('sobrenome'), email=request.POST.get('email'),
                            participante=True, curso=cursos[request.POST.get('curso')])
            usuario.save()

        try:
            minicurso = Atividade.objects.get(id=minic, inscricao_aberta=True)
            participacoes = Participacao.objects.filter(atividade=minicurso).count()

            if participacoes < minicurso.maximo_inscritos:
                    try:
                        participacao = Participacao.objects.get(atividade=minicurso, usuario=usuario)
                        response_data['result'] = 'JI'
                    except:
                        participacao = Participacao(atividade=minicurso, usuario=usuario, valido=True)
                        participacao.save()
                        response_data['result'] = 'IC'
            else:
                response_data['result'] = 'LE'

        except:
            response_data['result'] = 'MI'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def minicursos_antigos(request):
    ano_corrente = datetime.now().year
    minic_ant = Atividade.objects.filter(tipo='MN').exclude(data_inicial__year=ano_corrente).order_by('data_inicial').reverse()
    return render(request, 'atividade/antigos.html', {'minic_ant':minic_ant})


def certificados(request):
    atv = Atividade.objects.filter(certificado_disponivel=True)
    ano = Atividade.objects.dates('data_inicial', 'year').distinct().reverse()
    return render(request, 'atividade/certificados.html', {'anos':ano, 'atv': atv})


def buscacertificados(request):
    if request.method == 'POST':

        if request.POST.get('matricula') == "" or request.POST.get('atividade') == "":
            return HttpResponse(
                json.dumps({}),
                content_type="application/json"
            )

        response_data = {}
        matricula = int(request.POST.get('matricula'))
        atividadeid = int(request.POST.get('atividade'))

        usuario = Aluno.objects.defer('first_name', 'matricula', 'id').get(matricula=matricula)
        atividade = Atividade.objects.defer('nome', 'carga', 'local', 'data_inicial', 'data_final', 'aviso').get(id=atividadeid)
        certificado = Participacao.objects.filter(usuario=usuario, atividade=atividade)

        if certificado.__len__ == 0:
            return HttpResponse(
                json.dumps({}),
                content_type="application/json"
            )

        rp = {}
        js = {}
        for ct in certificado:
            if ct.valido:
                if ct.horas_validas==0:
                    carga=atividade.carga
                else:
                    carga=ct.horas_validas

                if ct.papel:
                    tipo = ct.papel
                else:
                    tipo = ""

                rp = {'atividade%d'%(ct.id):{'nome':usuario.first_name, 'atividade':atividade.nome, 'tipo':tipo, 'horas':carga, 'data_inicial':'%d/%d/%d'%(atividade.data_inicial.day, atividade.data_inicial.month, atividade.data_inicial.year), 'data_final':'%d/%d/%d'%(atividade.data_final.day, atividade.data_final.month, atividade.data_final.year)}}
                js.update(rp)

        #lista = list(usuario) + list(certificado) + list(atividade)
        #print (lista)


        #atividade = list(atividade)
        #atividade[0].aviso = "%s/%s" % (meses[str(atividade[0].data_inicial.month)], str(atividade[0].data_inicial.year))

        #nova_lista = list(atividade[0].nome, usuario=usuario.first_name, data=atividade[0].aviso)

        #rp = serializers.serialize('json', lista)

        print(js)
        #print(response_data)
        #print(rp)
        return HttpResponse(
            json.dumps(js),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



