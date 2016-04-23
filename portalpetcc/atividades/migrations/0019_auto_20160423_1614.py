# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0018_auto_20160423_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 14, 24, 653086)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 14, 24, 653033)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
