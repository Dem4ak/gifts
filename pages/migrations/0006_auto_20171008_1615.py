# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171006_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='show_in_header',
        ),
        migrations.RemoveField(
            model_name='page',
            name='show_upper_search',
        ),
    ]