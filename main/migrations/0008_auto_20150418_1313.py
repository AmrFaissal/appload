# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_app_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
