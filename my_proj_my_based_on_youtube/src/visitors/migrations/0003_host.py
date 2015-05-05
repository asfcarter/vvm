# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20150308_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32, null=True)),
                ('mobile', models.CharField(max_length=32, null=True)),
                ('company', models.CharField(max_length=32, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
