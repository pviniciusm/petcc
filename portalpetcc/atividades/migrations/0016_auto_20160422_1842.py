# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0015_auto_20160417_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='organizacao',
            field=models.CharField(default='PET - Ciência da Computação', max_length=100),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 22, 18, 42, 13, 74034)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 22, 18, 42, 13, 73979)),
        ),
    ]
