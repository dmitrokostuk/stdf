# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='exam_title',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443 '),
        ),
        migrations.AlterField(
            model_name='tests',
            name='notes',
            field=models.TextField(null=True, verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='tests',
            name='teacher',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447'),
        ),
    ]
