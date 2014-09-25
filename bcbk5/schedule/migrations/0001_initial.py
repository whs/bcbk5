# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('by', models.CharField(max_length=255)),
                ('room', models.SmallIntegerField(choices=[(0, b'17201'), (1, b'17302'), (2, b'17303'), (3, b'17304'), (4, b'17401'), (5, b'17402')])),
                ('slot', models.SmallIntegerField(choices=[(10, b'10:40 - 11:10'), (20, b'11:10 - 11:40'), (30, b'11:40 - 12:10'), (40, b'13:00 - 13:30'), (50, b'13:30 - 14:00'), (60, b'14:00 - 14:30'), (70, b'14:30 - 15:00'), (80, b'15:20 - 15:50'), (90, b'15:50 - 16:20'), (100, b'16:50 - 17:20')])),
                ('double', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
