# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift_ru', '0002_auto_20171006_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sliderimage',
            old_name='product',
            new_name='key',
        ),
    ]
