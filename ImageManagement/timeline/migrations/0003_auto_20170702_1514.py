# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20170702_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='comment_text',
            field=models.CharField(blank=True, default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='type',
            field=models.CharField(choices=[('like', 'like'), ('collect', 'collect'), ('comment', 'comment'), ('post', 'post')], max_length=10),
        ),
    ]
