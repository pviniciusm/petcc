# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='vertical',
            field=models.BooleanField(default=False, help_text='Opção para marcar quando a imagem da notícia for muito alta, para que não fique mal exibida'),
        ),
    ]
