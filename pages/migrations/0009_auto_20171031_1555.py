# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20171031_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_title', to='pages.Page', verbose_name='Родительская страница'),
        ),
    ]