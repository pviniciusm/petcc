# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0018_auto_20160423_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 4, 23, 16, 16, 9, 674633)),
        ),
    ]
