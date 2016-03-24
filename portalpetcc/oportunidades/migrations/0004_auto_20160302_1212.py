# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0003_auto_20160302_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='bolsa',
            field=models.CharField(help_text='Define o valor da bolsa, caso disponível', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='carga',
            field=models.IntegerField(help_text='Define a carga horária semanal', blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(default=datetime.datetime(2016, 3, 2, 12, 12, 19, 8364), blank=True),
        ),
    ]
