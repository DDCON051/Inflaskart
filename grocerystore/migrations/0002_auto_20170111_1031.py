# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['top_category']},
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'ordering': ['sub_category_1']},
        ),
        migrations.AlterModelOptions(
            name='productsubsubcategory',
            options={'ordering': ['sub_category_2']},
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='category',
            new_name='top_category',
        ),
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='subcategory1',
            new_name='parent_category',
        ),
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='subcat1',
            new_name='sub_category_1',
        ),
        migrations.RenameField(
            model_name='productsubsubcategory',
            old_name='subcategory2',
            new_name='parent_category',
        ),
        migrations.RenameField(
            model_name='productsubsubcategory',
            old_name='subcat2',
            new_name='sub_category_2',
        ),
    ]
