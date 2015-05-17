# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150516_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clue',
            name='hunt',
            field=models.ForeignKey(to='core.Hunt', related_name='clues'),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owned_hunts'),
        ),
        migrations.AlterField(
            model_name='hunt',
            name='participants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='joined_hunts'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='clue',
            field=models.ForeignKey(to='core.Clue', related_name='submissions'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='submissions'),
        ),
    ]
