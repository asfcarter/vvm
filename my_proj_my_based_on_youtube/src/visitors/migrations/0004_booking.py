# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.CharField(max_length=32)),
                ('end_time', models.CharField(max_length=32)),
                ('host', models.ForeignKey(to='visitors.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
