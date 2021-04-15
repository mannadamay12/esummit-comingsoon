from .models import *
from django import forms

class RegisterForm(forms.ModelForm):
	class Meta():
		model = Register
		fields = ['name','contact_no','email','thapar_student','unwind_interested','elevate_interested','bootcamp_interested']