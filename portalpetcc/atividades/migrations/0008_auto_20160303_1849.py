# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0007_auto_20160302_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 3, 3, 18, 49, 54, 537640)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 3, 3, 18, 49, 54, 537596)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='tipo',
            field=models.CharField(choices=[('MN', 'Minicurso'), ('PEC', 'PEC'), ('SEM', 'Seminario'), ('TA', 'Topico de Apoio'), ('PESQ', 'Topico de Apoio'), ('EX', 'Extensao'), ('OU', 'Outro')], default='OU', max_length=50),
        ),
    ]
