# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-08 01:42
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='题目答案'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='题目详情'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='status',
            field=models.BooleanField(default=1, verbose_name='审核状态'),
        ),
    ]