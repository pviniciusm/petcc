# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0007_auto_20160303_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(default=datetime.datetime(2016, 3, 5, 21, 49, 36, 156748), blank=True),
        ),
    ]
