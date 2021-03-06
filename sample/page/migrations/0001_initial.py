# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique_for_month='pubdate')),
                ('pubdate', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'BlogArticle',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('descriptions', models.TextField()),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='In Stock')),
                ('price', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.Category')),
            ],
            options={
                'ordering': ['-price', 'name'],
                'verbose_name_plural': 'Tovars',
                'db_table': 'Good',
                'verbose_name': 'Tovar',
            },
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together=set([('category', 'name')]),
        ),
    ]
