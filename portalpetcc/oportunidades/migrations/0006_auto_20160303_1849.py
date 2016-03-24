# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0005_auto_20160302_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 3, 3, 18, 49, 54, 540519)),
        ),
    ]
