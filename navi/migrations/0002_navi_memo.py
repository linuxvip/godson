# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navi',
            name='memo',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
    ]
