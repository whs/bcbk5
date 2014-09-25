# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('profession', models.CharField(max_length=255, blank=True)),
                ('work', models.CharField(max_length=255, blank=True)),
                ('twitter', models.CharField(max_length=15, blank=True)),
                ('web', models.URLField(blank=True)),
                ('interests', models.CharField(max_length=255, blank=True)),
                ('shirt', models.IntegerField(default=1)),
                ('food', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
