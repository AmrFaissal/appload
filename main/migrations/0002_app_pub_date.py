# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 14, 23, 6, 21, 3623, tzinfo=utc)),
        ),
    ]
