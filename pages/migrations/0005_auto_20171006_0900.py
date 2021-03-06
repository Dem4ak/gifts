# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_show_in_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_upper_search',
            field=models.BooleanField(default=False, verbose_name='отображать над поиском'),
        ),
        migrations.AlterField(
            model_name='page',
            name='show_in_header',
            field=models.BooleanField(default=False, verbose_name='отображать в шапке'),
        ),
    ]
