# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-12 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20190109_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='huaban',
            name='imgdiscrit',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
