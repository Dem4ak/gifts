# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20171009_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.ManyToManyField(blank=True, default=25, to='products.ProductCategory', verbose_name='Главная категория'),
        ),
    ]