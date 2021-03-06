# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-11 20:53
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standardpage', '0004_auto_20161211_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph.html')), ('header', wagtail.wagtailcore.blocks.StructBlock((('header_text', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Header', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))), classname='title', icon='fa-header', template='blocks/header.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, required=False)), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Select an image size'), ('fit', 'Fit-to-text-width'), ('full', 'Full-width'), ('square', 'Square')], required=False))), icon='image', template='blocks/image.html')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('attribute_name', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False)), ('attribute_group', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Fugazi', required=False))), icon='openquote', template='blocks/blockquote.html')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='embed', template='blocks/embed.html'))), blank=True),
        ),
    ]
