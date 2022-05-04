from django.db import models
from django.contrib.auth.models import User


class Stacks(models.Model):
	nameCompany = models.CharField(max_length=30)
	nameSystem = models.CharField(max_length=30)
	versionSystem = models.CharField(max_length=30)
	vendeur = models.CharField(max_length=30)
	typeSystem = models.CharField(max_length=30)
	
	def __str__(self):
		return self.nameCompany


class Alert(models.Model):
	nomAlert = models.CharField(max_length=30)
	descriptionAlert = models.CharField(max_length=5000)
	sousValeurAlert = models.CharField(max_length=50)

	def __str__(self):
		return self.nomAlert 