# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0009_auto_20160303_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='integrantes',
            field=models.CharField(max_length=150, default='', blank=True, help_text='Usar para projetos de pesquisa, indicando os participantes doprojeto.'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 3, 5, 21, 49, 36, 152612)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 3, 5, 21, 49, 36, 152559)),
        ),
    ]
