# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 09:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membranes', '0005_auto_20171219_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membrane',
            name='curator',
        ),
        migrations.AddField(
            model_name='membrane',
            name='curator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
