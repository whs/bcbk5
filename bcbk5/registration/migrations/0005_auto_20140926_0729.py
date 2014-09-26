# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20140925_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='car_license',
            field=models.CharField(default=b'', max_length=8, verbose_name=b'Car license number'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registration',
            name='food_allergic',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Food allergic'),
            preserve_default=True,
        ),
    ]
