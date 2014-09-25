# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='food',
            field=models.IntegerField(default=0, choices=[(0, b'Normal'), (1, b'Halal'), (2, b'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='shirt',
            field=models.IntegerField(default=1, choices=[(0, b'S'), (1, b'M'), (2, b'L'), (3, b'XL'), (4, b'XXL')]),
        ),
    ]
