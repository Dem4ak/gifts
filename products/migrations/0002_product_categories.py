# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory', verbose_name='Категории'),
            preserve_default=False,
        ),
    ]
