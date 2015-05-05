# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('mobile', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('mobile', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='car',
            name='host',
            field=models.ForeignKey(to='visitors.Host'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='visitor',
            field=models.ForeignKey(to='visitors.Visitor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='host',
            field=models.ForeignKey(to='visitors.Host'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='visitor',
            field=models.ForeignKey(to='visitors.Visitor'),
            preserve_default=True,
        ),
    ]
