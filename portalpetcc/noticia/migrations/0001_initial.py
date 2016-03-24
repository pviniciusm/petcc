# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import noticia.models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('visualizacoes', models.IntegerField(auto_created=True, editable=False, default=0)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('titulo', models.CharField(max_length=150)),
                ('conteudo', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True, blank=True)),
                ('image', models.ImageField(blank=True, upload_to=noticia.models.get_img_path)),
                ('vertical', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
