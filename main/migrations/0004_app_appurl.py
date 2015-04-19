# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150414_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='appUrl',
            field=models.CharField(default='', max_length=100),
        ),
    ]
