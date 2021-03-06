# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0011_auto_20160912_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewartistrelationship',
            old_name='ArtistRelationship',
            new_name='page',
        ),
        migrations.AlterField(
            model_name='reviewartistrelationship',
            name='artist',
            field=models.ForeignKey(help_text='The artist who made the album being reviewed', on_delete=django.db.models.deletion.CASCADE, related_name='artist_review_relationship', to='artist.Artist'),
        ),
    ]
