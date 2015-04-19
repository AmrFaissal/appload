# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_app_appurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='appUrl',
        ),
        migrations.AddField(
            model_name='app',
            name='zipfile',
            field=models.FileField(upload_to='media/%Y/%m/%d', default=datetime.datetime(2015, 4, 17, 14, 25, 25, 992598, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
