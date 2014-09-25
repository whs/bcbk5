# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20140925_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='food',
            field=models.SmallIntegerField(default=0, choices=[(0, b'Normal'), (1, b'Halal'), (2, b'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='shirt',
            field=models.SmallIntegerField(default=1, choices=[(0, b'S'), (1, b'M'), (2, b'L'), (3, b'XL'), (4, b'XXL')]),
        ),
    ]
