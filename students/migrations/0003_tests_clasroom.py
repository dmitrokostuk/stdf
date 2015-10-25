# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151018_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='clasroom',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
