# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_visitor_llast_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='llast_name',
        ),
    ]
