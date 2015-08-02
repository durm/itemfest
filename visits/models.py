from django.db import models
from checks.models import Check

# Create your models here.
class Visit(models.Model):
	name = models.CharField(max_length=512)
	desc = models.TextField(blank=True)
	checks = models.ManyToManyField(Check, blank=True)
	
	def __unicode__(self):
		return self.name