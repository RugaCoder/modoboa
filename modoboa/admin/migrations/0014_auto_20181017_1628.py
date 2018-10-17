# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0013_auto_20180124_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='default_mailbox_quota',
            field=models.PositiveIntegerField(default=0, verbose_name='Default mailbox quota'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='quota',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
