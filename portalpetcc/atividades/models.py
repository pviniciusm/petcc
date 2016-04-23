from django.db import models
from datetime import datetime
from home.models import User, Aluno
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.defaultfilters import slugify


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
    slug = models.SlugField(max_length=100, blank=True, unique=True)
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
    organizacao = models.CharField(max_length=100, default="PET - Ciência da Computação", blank=False, null=False)

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

    def get_absolute_url(self):
        return reverse(
            'projetos.views.atividades',
            kwargs={'slug': self.slug}
        )


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


def atividade_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        string = "%s %s %s" % (tipos[instance.tipo], instance.nome, str(instance.data_inicial.year))
        slug = slugify(string)
        novo_slug = slug
        contador = 0

        while Atividade.objects.filter(
            slug=novo_slug
        ).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug


signals.pre_save.connect(atividade_pre_save, sender=Atividade)
