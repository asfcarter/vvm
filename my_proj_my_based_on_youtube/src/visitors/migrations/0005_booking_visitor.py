# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='visitor',
            field=models.ForeignKey(to='visitors.Visitor', null=True),
            preserve_default=True,
        ),
    ]
