# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=512)
	desc = models.TextField(blank=True)
	image = models.ImageField(upload_to="products", blank=True)
	price = models.FloatField()
	
	def __unicode__(self):
		return self.name
		
	def get_ingredient_fractions(self):
		return IngredientFraction.objects.filter(product=self)
	
class Ingredient(models.Model):
	name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name
	
class IngredientFraction(models.Model):
	product = models.ForeignKey(Product)
	ingredient = models.ForeignKey(Ingredient)
	mass = models.FloatField()
	
	def __unicode__(self):
		return u"{0}: {1} - {2}".format(self.product.name, self.ingredient.name, self.mass)