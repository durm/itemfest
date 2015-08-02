from django.db import models
from products.models import Product

class Position(models.Model):
	product = models.ForeignKey(Product)
	price = models.FloatField()
	
	def __unicode__(self):
		return "{0} {1}".format(self.product.name, self.price)

class Check(models.Model):
	name = models.CharField(max_length=512)
	desc = models.TextField(blank=True)
	positions = models.ManyToManyField(Position, blank=True)
	
	def __unicode__(self):
		return self.name