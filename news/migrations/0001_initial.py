# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 09:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок новости')),
                ('slug', models.SlugField(help_text='Адрес новости на латинице. Например, "your_address"', max_length=200, unique=True, verbose_name='Адрес')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Содержимое новости')),
                ('visible', models.BooleanField(default=True, verbose_name='отображать')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='заголовок')),
                ('meta_keywords', models.CharField(blank=True, max_length=250, verbose_name='ключевые слова')),
                ('meta_description', models.TextField(blank=True, verbose_name='описание')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('changed', models.DateTimeField(auto_now=True, null=True, verbose_name='дата изменения')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='заголовок')),
                ('meta_keywords', models.CharField(blank=True, max_length=250, verbose_name='ключевые слова')),
                ('meta_description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория новости',
                'verbose_name_plural': 'Категория новости',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.NewsCategory'),
        ),
    ]
