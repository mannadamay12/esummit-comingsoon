from .models import *
from django import forms

class EmailForm(forms.ModelForm):
	class Meta():
		model = Subscriber
		fields = ['email']
