# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20171009_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='products.ProductCategory', verbose_name='Категории'),
        ),
    ]
