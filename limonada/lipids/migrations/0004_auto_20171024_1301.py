# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipids', '0003_auto_20171024_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lipid',
            name='slug',
            field=models.SlugField(),
        ),
    ]