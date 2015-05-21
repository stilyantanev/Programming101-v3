# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('rating', models.FloatField()),
                ('year', models.DateField()),
                ('running_time', models.TimeField()),
                ('cover', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('movie_format', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(to='website.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projection', models.ForeignKey(to='website.Projections')),
            ],
        ),
    ]
