# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipids', '0016_auto_20180110_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='lipid',
            name='l4_class',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
