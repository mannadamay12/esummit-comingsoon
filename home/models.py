from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Register(models.Model):

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


    name                = models.CharField(max_length=100)
    contact_no          = PhoneNumberField(blank=False)
    email               = models.EmailField(verbose_name="Email Address")
    thapar_student      = models.BooleanField(choices=BOOL_CHOICES)
    unwind_interested   = models.BooleanField(default=True)
    elevate_interested  = models.BooleanField(default=True)
    bootcamp_interested = models.BooleanField(default=True)
	
    def __str__(self):
       return self.name