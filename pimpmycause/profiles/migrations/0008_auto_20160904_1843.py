# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20160904_1833'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CauseUser',
            new_name='CauseProfile',
        ),
        migrations.RenameModel(
            old_name='MarketerUser',
            new_name='MarketerProfile',
        ),
    ]