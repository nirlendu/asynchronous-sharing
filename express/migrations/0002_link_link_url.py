# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
