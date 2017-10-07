# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 11:51
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift_ru', '0003_auto_20171006_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Текст шага')),
                ('title', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_ru.Home', verbose_name='Заголовок шага')),
            ],
            options={
                'verbose_name_plural': 'Шаги оформления',
                'verbose_name': 'Шаг оформления',
            },
        ),
    ]
