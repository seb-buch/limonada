# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-20 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20171220_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[homepage.models.validate_year]),
        ),
    ]
