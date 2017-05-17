# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170516_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='radioUserProfileChest',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('honeycombing', models.CharField(default='N', max_length=1)),
                ('septal', models.CharField(default='NULL', max_length=15)),
                ('groundGlass', models.CharField(default='NULL', max_length=15)),
                ('consolidation', models.CharField(default='NULL', max_length=25)),
                ('fibrosis', models.CharField(default='NULL', max_length=15)),
                ('nodules', models.CharField(default='NULL', max_length=15)),
                ('massLesion', models.CharField(default='N', max_length=1)),
                ('treeInBudLesion', models.CharField(default='N', max_length=1)),
                ('airTrapping', models.CharField(default='N', max_length=1)),
                ('mosaicAttenuation', models.CharField(default='N', max_length=1)),
                ('bronchiectasis', models.CharField(default='NULL', max_length=15)),
                ('cavity', models.CharField(default='NULL', max_length=15)),
                ('cysts', models.CharField(default='NULL', max_length=15)),
                ('emphysema', models.CharField(default='N', max_length=1)),
                ('lymphNodes', models.CharField(default='NULL', max_length=15)),
                ('pleuralEffusion', models.CharField(default='N', max_length=1)),
                ('pleuralThickening', models.CharField(default='NULL', max_length=15)),
                ('crazyPaving', models.CharField(default='N', max_length=1)),
                ('haloSign', models.CharField(default='N', max_length=1)),
                ('reverseHalo', models.CharField(default='N', max_length=1)),
                ('fat', models.CharField(default='N', max_length=1)),
                ('heart', models.CharField(default='NULL', max_length=15)),
            ],
        ),
    ]
