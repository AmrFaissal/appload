# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150418_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='zipfile',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
