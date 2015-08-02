# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=512)
	desc = models.TextField(blank=True)
	image = models.ImageField(upload_to="products", blank=True)
	price = models.FloatField()
	
	def __unicode__(self):
		return self.name