# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0008_auto_20160303_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 3, 3, 18, 51, 52, 881056)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 3, 3, 18, 51, 52, 881019)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='tipo',
            field=models.CharField(choices=[('MN', 'Minicurso'), ('PEC', 'PEC'), ('SEM', 'Seminario'), ('TA', 'Topico de Apoio'), ('PESQ', 'Pesquisa'), ('EX', 'Extensao'), ('OU', 'Outro')], default='OU', max_length=50),
        ),
    ]
