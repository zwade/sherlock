# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150517_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunt',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='comment',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
