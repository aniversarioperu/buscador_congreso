# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_statistic_statistic_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]
