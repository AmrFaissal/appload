from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class App(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	public = models.BooleanField(default=True, blank=True)
	zipfile = models.FileField(upload_to='uploads')

	def __str__(self):
		return "{0}: {1} @{2}".format(self.name, self.description, self.zipfile.url)

