# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='tags',
            field=models.ManyToManyField(to='images.ImageTag'),
        ),
    ]