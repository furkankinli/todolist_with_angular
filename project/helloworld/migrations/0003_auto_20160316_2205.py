# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20160315_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='value',
            field=models.IntegerField(default=10),
        ),
    ]
