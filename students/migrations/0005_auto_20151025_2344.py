# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20151025_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tests',
            old_name='date',
            new_name='examtime',
        ),
    ]
