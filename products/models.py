# -*- coding: utf-8 -*-

from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name
	
class IngredientFraction(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	mass = models.FloatField()
	
	def __unicode__(self):
		return "{0} {1}".format(self.ingredient.name, self.mass)
		
class Product(models.Model):
	name = models.CharField(max_length=512)
	desc = models.TextField(blank=True)
	image = models.ImageField(upload_to="products", blank=True)
	price = models.FloatField()
	ingredient_fractions = models.ManyToManyField(IngredientFraction)
	
	def __unicode__(self):
		return self.name
		
