from django.shortcuts import render
from .forms import *
# Create your views here.
def subscribe(request):
	if(request.method == 'POST'):
		form = EmailForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	
	form = EmailForm()
	context = {
		'form' : form,
	}
	return render(request, 'home/comingsoon.html', context)

def gallery(request):
	return render(request, 'home/gallery.html')
