# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20140925_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(default='', max_length=75, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='food',
            field=models.SmallIntegerField(default=0, verbose_name=b'Food preference', choices=[(0, b'Normal'), (1, b'Halal'), (2, b'Vegetarian')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='shirt',
            field=models.SmallIntegerField(default=1, verbose_name=b'Shirt size', choices=[(0, b'S'), (1, b'M'), (2, b'L'), (3, b'XL'), (4, b'XXL')]),
        ),
    ]
