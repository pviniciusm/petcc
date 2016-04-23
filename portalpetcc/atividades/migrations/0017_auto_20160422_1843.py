# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0016_auto_20160422_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime(2016, 4, 22, 18, 43, 10, 47754)),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime(2016, 4, 22, 18, 43, 10, 47701)),
        ),
    ]
