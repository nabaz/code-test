# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-17 03:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171214_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difference',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='difference',
            name='value',
            field=models.IntegerField(),
        ),
    ]
