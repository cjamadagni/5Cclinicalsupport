# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20170608_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicuserprofile',
            name='eosinophilia',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
