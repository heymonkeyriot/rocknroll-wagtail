# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-23 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feature_content_page', '0010_auto_20161006_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenrefeaturepagerelationship',
            name='page',
        ),
        migrations.RemoveField(
            model_name='subgenrefeaturepagerelationship',
            name='subgenre',
        ),
        migrations.DeleteModel(
            name='SubGenreFeaturePageRelationship',
        ),
    ]