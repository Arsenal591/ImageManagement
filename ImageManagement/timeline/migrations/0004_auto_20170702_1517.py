# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20170702_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='receiver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receives', to='users.MyUser'),
        ),
    ]