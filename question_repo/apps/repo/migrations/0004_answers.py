# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-08 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repo', '0003_questionscollection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='学生答案')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Questions', verbose_name='题目')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='答题人')),
            ],
            options={
                'verbose_name': '答题记录',
                'verbose_name_plural': '答题记录',
            },
        ),
    ]