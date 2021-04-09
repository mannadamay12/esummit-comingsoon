from django.db import models

class Subscribe(models.Model):

	email 				= models.EmailField(verbose_name="email_id")
	
	def __str__(self):
		return self.email
