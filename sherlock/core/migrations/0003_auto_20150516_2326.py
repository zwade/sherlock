# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clue_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='slug',
            field=models.CharField(blank=True, unique=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
