# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 10:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ukPolice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='country',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='stateOrProvince',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='url',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='user',
        ),
        migrations.RemoveField(
            model_name='crime',
            name='zipCode',
        ),
    ]
