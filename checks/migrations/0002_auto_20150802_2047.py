# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='positions',
            field=models.ManyToManyField(to='checks.Position', blank=True),
        ),
    ]
