# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=500)),
                ('points', models.IntegerField()),
                ('hunt', models.ForeignKey(to='core.Hunt')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='submissions')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('valid', models.BooleanField()),
                ('verified', models.BooleanField()),
                ('clue', models.ForeignKey(to='core.Clue')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
