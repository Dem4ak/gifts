# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gift_ru.models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_ru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gift_ru.models.FilePathPhotos)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Слайды',
                'verbose_name': 'Слайд',
            },
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.RemoveField(
            model_name='home',
            name='slider_images',
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_ru.Home'),
        ),
    ]
