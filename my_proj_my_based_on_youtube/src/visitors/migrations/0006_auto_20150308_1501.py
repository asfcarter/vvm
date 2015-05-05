# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0005_booking_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(verbose_name=b'end time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(verbose_name=b'start time'),
            preserve_default=True,
        ),
    ]
