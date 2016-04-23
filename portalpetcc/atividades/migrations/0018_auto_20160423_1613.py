# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0017_auto_20160422_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 13, 31, 445237)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 13, 31, 445184)),
        ),
    ]
