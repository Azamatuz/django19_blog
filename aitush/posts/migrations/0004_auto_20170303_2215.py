# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170303_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
