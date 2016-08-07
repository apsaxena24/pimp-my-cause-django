# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimpuser',
            name='linkedin',
            field=models.CharField(default='http://twitter.com', max_length=30),
        ),
        migrations.AddField(
            model_name='pimpuser',
            name='twitter',
            field=models.CharField(default='http://linkedin.com', max_length=30),
        ),
    ]