# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 08:13
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20171008_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=mptt.fields.TreeManyToManyField(blank=True, db_index=True, null=True, related_name='_productcategory_parent_+', to='products.ProductCategory'),
        ),
    ]
