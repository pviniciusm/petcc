# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0020_auto_20160423_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='slug',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 16, 9, 671752)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 16, 16, 9, 671703)),
        ),
    ]
