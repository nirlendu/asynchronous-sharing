# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('express', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='broadcast_parent_id',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='expression',
            name='expression_imagefile',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='expression',
            name='expression_link_id',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_desc',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_image',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
