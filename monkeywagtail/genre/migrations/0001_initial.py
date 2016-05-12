# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-08 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, help_text='The parent genre e.g. metal', max_length=254, verbose_name='The genre')),
                ('sub_genre', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.TextBlock(icon='fa-music', label='Death metal, black metal etc.')),))),
            ],
        ),
    ]