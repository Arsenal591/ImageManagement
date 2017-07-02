# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170701_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='blacklist',
            field=models.ManyToManyField(blank=True, related_name='blacked', to='users.MyUser'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followers', to='users.MyUser'),
        ),
    ]
