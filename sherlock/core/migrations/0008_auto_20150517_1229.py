# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150517_1224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together=set([]),
        ),
    ]
