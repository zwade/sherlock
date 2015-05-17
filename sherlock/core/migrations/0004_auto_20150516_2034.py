# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150516_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clue',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='participants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
