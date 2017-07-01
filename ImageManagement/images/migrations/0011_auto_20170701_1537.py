# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20170701_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='img',
            field=models.ImageField(null=True, upload_to='image_poll'),
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='tags',
            field=models.ManyToManyField(null=True, to='images.ImageTag'),
        ),
    ]