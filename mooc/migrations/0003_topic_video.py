# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_topic_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='video',
            field=models.FileField(default='video', upload_to='videos/'),
        ),
    ]
