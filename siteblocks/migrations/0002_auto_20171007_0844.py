# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteblocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['order', 'pk'], 'verbose_name': 'меню', 'verbose_name_plural': 'меню'},
        ),
    ]