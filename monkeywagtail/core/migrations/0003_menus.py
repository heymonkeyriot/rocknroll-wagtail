# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-18 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160702_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Menu title')),
                ('menu', wagtail.wagtailcore.fields.StreamField((('link', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='fa-link')), ('external_link', wagtail.wagtailcore.blocks.URLBlock(icon='fa-link')), ('link_text', wagtail.wagtailcore.blocks.CharBlock())), icon='link')),), blank=True, verbose_name='Songs')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
