# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]