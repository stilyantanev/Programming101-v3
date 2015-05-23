# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150520_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('movie_format', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projection', models.ForeignKey(to='website.Projection')),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RemoveField(
            model_name='projections',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='projection',
        ),
        migrations.DeleteModel(
            name='Projections',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
        migrations.AddField(
            model_name='projection',
            name='movie',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
