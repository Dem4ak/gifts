# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество товара'),
        ),
    ]