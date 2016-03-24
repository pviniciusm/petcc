from django.db import models
from datetime import datetime
from home.models import User, Aluno


tipos={
    'MN':'Minicurso',
    'PEC': 'Palestra',
    'SEM': 'Seminário',
    'TA': 'Tópico de Apoio',
    'PESQ': 'Pesquisa',
    'EX': 'Extensão',
    'OU': 'Projeto'
}
# Create your models here.
class Atividade(models.Model):
    nome = models.CharField(max_length=150)
    carga = models.IntegerField()
    local = models.CharField(max_length=150, default="")
    data_inicial = models.DateField(
            default=datetime.now,
            blank=False
    )
    data_final = models.DateField(
            default=datetime.now,
            blank=False
    )
    hora_inicial = models.TimeField(
        default=datetime.now(),
        blank=False
    )
    hora_final = models.TimeField(
        default=datetime.now(),
        blank=False
    )
    data_definida = models.BooleanField(default=False)
    certificado_disponivel = models.BooleanField(default=False)
    inscricao_aberta = models.BooleanField(default=False)
    maximo_inscritos = models.IntegerField(default=30, blank=True)

    tipo = models.CharField(max_length=50, choices=(('MN', 'Minicurso'), ('PEC', 'PEC'), ('SEM', 'Seminario'),
                                                    ('TA', 'Topico de Apoio'), ('PESQ', 'Pesquisa'),
                                                    ('EX', 'Extensao'), ('OU', 'Outro')), default='OU')

    descricao = models.TextField()
    aviso = models.TextField(default="", blank=True)
    integrantes = models.CharField(max_length=150, blank=True, default="", help_text="Usar para projetos de pesquisa, "
                                                                                     "indicando os participantes do"
                                                                                     "projeto.")

    def __unicode__(self):
        return "%s" % self.nome

    def __str__(self):
        return "%s - %s (%s)" % (tipos[self.tipo], self.nome, self.data_inicial.year)

    def ano(self):
        return self.data_inicial.year

    class Meta:
        ordering = ['-data_inicial']


class Participacao(models.Model):
    atividade = models.ForeignKey(Atividade)
    usuario = models.ForeignKey(Aluno, null=True)
    valido = models.BooleanField(blank=False, default=False)
    papel = models.CharField(max_length=120, blank=True, default="Ouvinte")
    horas_validas = models.IntegerField(blank=True, default=0,help_text='Total de horas validas para a atividade. '
                                                                        'Deixar 0 caso for a carag total cadastrada na '
                                                                        'atividade')

    def __unicode__(self):
        return "%s" % self.id

    def nome_atividade(self):
        return self.atividade.nome

    def nome_participante(self):
        return self.usuario.__str__()

    def ano(self):
        return self.atividade.data_inicial.year

    def mes(self):
        return self.atividade.data_inicial.month

    def tipo(self):
        return self.atividade.tipo

    def matricula(self):
        return self.usuario.matricula

    def show(self):
        return self.atividade.__str__()
