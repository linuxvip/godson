# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180315_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='asset_no',
        ),
        migrations.RemoveField(
            model_name='host',
            name='cpu_model',
        ),
        migrations.RemoveField(
            model_name='host',
            name='vendor',
        ),
    ]
