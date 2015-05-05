# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='company',
            field=models.CharField(max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visitor',
            name='email',
            field=models.CharField(max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visitor',
            name='mobile',
            field=models.CharField(max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='first_name',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='last_name',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
