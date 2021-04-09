from .models import *
from django import forms

class EmailForm(forms.ModelForm):
	class Meta():
		model = Subscribe
		fields = ['email']
