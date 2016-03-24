from django.contrib import admin
from atividades.models import *


# Register your models here.
class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_participante', 'show', 'matricula', 'nome_atividade', 'ano',)
    pass


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'ano', 'inscricao_aberta', 'certificado_disponivel')
    pass

admin.site.register(Participacao, ParticipacaoAdmin)
admin.site.register(Atividade, AtividadeAdmin)
