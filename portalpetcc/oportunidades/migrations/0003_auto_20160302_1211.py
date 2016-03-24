# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0002_auto_20160302_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(default=datetime.datetime(2016, 3, 2, 12, 11, 42, 967250), blank=True),
        ),
    ]
