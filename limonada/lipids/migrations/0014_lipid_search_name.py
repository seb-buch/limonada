# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-08 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipids', '0013_auto_20180105_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='lipid',
            name='search_name',
            field=models.CharField(default='temp', max_length=200),
            preserve_default=False,
        ),
    ]
