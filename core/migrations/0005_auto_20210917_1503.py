# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-17 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210917_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='text',
            new_name='content',
        ),
    ]
