# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-09 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
