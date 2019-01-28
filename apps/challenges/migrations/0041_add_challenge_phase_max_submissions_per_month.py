# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-12 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0040_change_broker_url_name_to_queue'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengephase',
            name='max_submissions_per_month',
            field=models.PositiveIntegerField(db_index=True, default=100000),
        ),
    ]