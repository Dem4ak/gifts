# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171031_0033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='Главная категории'),
            preserve_default=False,
        ),
    ]