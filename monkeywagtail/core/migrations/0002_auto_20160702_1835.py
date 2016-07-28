# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-02 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('wagtailcore', '0028_merge'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuMenuItemRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, help_text='Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name='External link')),
                ('link_document', models.ForeignKey(blank=True, help_text='Choose an existing document if you want the link to open a document.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, help_text='Choose an existing page if you want the link to point somewhere inside the CMS.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('links_in_menu', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='core.Menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='linkfields',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='linkfields',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='linkfields_ptr',
        ),
        migrations.RemoveField(
            model_name='menumenuitem',
            name='menuitem_ptr',
        ),
        migrations.RemoveField(
            model_name='menumenuitem',
            name='parent',
        ),
        migrations.DeleteModel(
            name='LinkFields',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='MenuMenuItem',
        ),
    ]
