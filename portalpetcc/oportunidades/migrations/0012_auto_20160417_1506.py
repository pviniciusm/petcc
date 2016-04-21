# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0011_auto_20160417_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 4, 17, 15, 6, 48, 262873)),
        ),
    ]
