# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150803_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ingredient_fractions',
        ),
        migrations.AddField(
            model_name='ingredientfraction',
            name='product',
            field=models.ForeignKey(default=1, to='products.Product'),
            preserve_default=False,
        ),
    ]
