# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 14:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('articles', '0004_auto_20171014_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('slug', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Article type',
                'verbose_name_plural': 'Article types',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.ArticleType', verbose_name='Type'),
        ),
    ]
