# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=50)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=50)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('username', models.CharField(unique=True, blank=True, verbose_name='username', max_length=30)),
                ('participante', models.BooleanField(default=False)),
                ('matricula', models.CharField(unique=True, blank=True, max_length=100)),
                ('curso', models.CharField(blank=True, max_length=100, default='Ciencia da Computacao')),
            ],
        ),
    ]
