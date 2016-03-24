# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0004_auto_20160302_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidade',
            name='edital',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='oportunidade',
            name='data_limite',
            field=models.DateField(default=datetime.datetime(2016, 3, 2, 12, 28, 46, 14257), blank=True),
        ),
    ]
