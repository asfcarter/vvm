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
            name='llast_name',
            field=models.CharField(default='eee', max_length=32),
            preserve_default=False,
        ),
    ]
