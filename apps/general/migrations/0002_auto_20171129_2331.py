# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='drillbit',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='motive',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='polymer',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='section',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='state',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='status',
            field=models.CharField(default='A', max_length=3),
        ),
    ]
