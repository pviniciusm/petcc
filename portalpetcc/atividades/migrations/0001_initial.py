# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=150)),
                ('carga', models.IntegerField()),
                ('local', models.CharField(max_length=150, default='')),
                ('data_inicial', models.DateField(default=datetime.datetime.now)),
                ('data_final', models.DateField(default=datetime.datetime.now)),
                ('hora_inicial', models.TimeField(default=datetime.datetime(2016, 2, 29, 19, 0, 58, 709812))),
                ('hora_final', models.TimeField(default=datetime.datetime(2016, 2, 29, 19, 0, 58, 709863))),
                ('data_definida', models.BooleanField(default=False)),
                ('certificado_disponivel', models.BooleanField(default=False)),
                ('inscricao_aberta', models.BooleanField(default=False)),
                ('maximo_inscritos', models.IntegerField(blank=True, default=30)),
                ('tipo', models.CharField(max_length=50, choices=[('MN', 'Minicurso'), ('PEC', 'PEC'), ('SEM', 'Seminario'), ('TA', 'Topico de Apoio'), ('EX', 'Extensao'), ('OU', 'Outro')], default='OU')),
                ('descricao', models.TextField()),
                ('aviso', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ['-data_inicial'],
            },
        ),
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('valido', models.BooleanField(default=False)),
                ('papel', models.CharField(blank=True, max_length=120, default='Ouvinte')),
                ('horas_validas', models.IntegerField(blank=True, help_text='Total de horas validas para a atividade. Deixar 0 caso for a carag total cadastrada na atividade', default=0)),
                ('atividade', models.ForeignKey(to='atividades.Atividade')),
                ('usuario', models.ForeignKey(to='home.Aluno', null=True)),
            ],
        ),
    ]
