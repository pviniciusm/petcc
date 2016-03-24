# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='bolsa',
            field=models.CharField(help_text='Define o valor da bolsa, caso disponível', max_length=30),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='carga',
            field=models.IntegerField(help_text='Define a carga horária semanal'),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='local',
            field=models.CharField(help_text='Local onde será relizado o projeto/estágio', max_length=50),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='texto',
            field=models.TextField(help_text='Descrição da oportunidade', max_length=500),
        ),
    ]
