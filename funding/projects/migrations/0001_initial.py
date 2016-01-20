# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 10:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('website', models.URLField(max_length=100)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('function', models.CharField(max_length=200)),
                ('maintainers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('added', models.CharField(max_length=100)),
                ('needs', models.TextField()),
                ('funding_status', models.CharField(max_length=20)),
                ('funding_status_notes', models.TextField()),
            ],
        ),
    ]
