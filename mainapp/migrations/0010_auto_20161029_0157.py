# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20161029_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectskills',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Project'),
        ),
    ]
