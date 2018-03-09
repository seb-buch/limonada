# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-05 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import lipids.models


class Migration(migrations.Migration):

    dependencies = [
        ('lipids', '0011_auto_20180105_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lipid',
            name='img',
            field=models.FileField(null=True, upload_to=lipids.models.img_path, validators=[lipids.models.validate_file_extension]),
        ),
    ]