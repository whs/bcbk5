# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20140926_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='car_license',
        ),
    ]
