# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelChannelRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_one_id', models.CharField(max_length=8)),
                ('channel_two_id', models.CharField(max_length=8)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ChannelPersonRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=8)),
                ('person_id', models.CharField(max_length=12)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ChannelPrimary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=30)),
                ('total_followers', models.IntegerField(default=0)),
                ('channel_weight', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('channel_created', models.DateTimeField(auto_now_add=True)),
                ('channel_updated', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ExpressionChannelRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=8)),
                ('expression_id', models.CharField(max_length=20)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='expressionchannelrelation',
            unique_together=set([('channel_id', 'expression_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='channelpersonrelation',
            unique_together=set([('channel_id', 'person_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='channelchannelrelation',
            unique_together=set([('channel_one_id', 'channel_two_id')]),
        ),
    ]
