# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-23 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0006_auto_20160913_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenreclass',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subgenreclass',
            name='slug',
        ),
        migrations.AlterField(
            model_name='subgenreclass',
            name='title',
            field=models.CharField(help_text="Be as esoteric as you'd like. This displays on the genre page as a list to end users", max_length=255),
        ),
    ]
