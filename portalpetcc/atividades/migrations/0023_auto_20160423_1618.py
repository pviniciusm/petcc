# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0022_auto_20160423_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 18, 53, 928570)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 18, 53, 928518)),
        ),
    ]
