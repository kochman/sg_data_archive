# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170503_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
