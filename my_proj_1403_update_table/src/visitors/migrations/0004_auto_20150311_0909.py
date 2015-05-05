# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_remove_visitor_llast_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='anpr',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='greeted',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
