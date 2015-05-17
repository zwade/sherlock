# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150516_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunt',
            name='slug',
            field=models.SlugField(max_length=8, unique=True, blank=True),
        ),
    ]
