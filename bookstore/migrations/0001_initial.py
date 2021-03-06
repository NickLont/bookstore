# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-25 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sat', 'Satire'), ('dra', 'Drama'), ('act', 'Action'), ('mys', 'Mystery'), ('chi', 'Childrens'), ('tra', 'Travel'), ('bio', 'Biography')], default='act', max_length=3)),
                ('info', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Category'),
        ),
    ]
