# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientFraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mass', models.FloatField()),
                ('ingredient', models.ForeignKey(to='products.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ingredient_fractions',
            field=models.ManyToManyField(to='products.IngredientFraction'),
        ),
    ]
