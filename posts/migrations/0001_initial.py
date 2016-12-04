# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-04 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('post_count', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('img_url', models.CharField(blank=True, max_length=500)),
                ('read_count', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
