from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
# Create your views here.


def subscribe(request):
	if(request.method == 'POST'):
		form = EmailForm(request.POST, request.FILES)
		if form.is_valid():
			messages.add_message(request, messages.INFO, 'Thank You for subscribing!')
			email = form.cleaned_data.get('email')
			form.save()
			send_mail(
                        'E-Summit 21', 
                        f"""Dear Participant,,
I hope this email finds you in the best of your health. We at EDC, thank you for signing up for E-Summit'21. We are extremely excited and glad that you could join us on this journey to revive the hustle.

With this fiesta around the corner, you will get your regular updates on events and all other further information on the mail itself.

We hope you savor this journey of new challenges, unlimited ideas, and untiring zeal.

Cheers,
Team EDC
                        """, 
                        'esummit@edctiet.com',
                        [email],
                    )
			return redirect('subscribe')
	
	form = EmailForm()
	context = {
		'form' : form,
	}
	return render(request, 'home/comingsoon.html', context)

def gallery(request):
	return render(request, 'home/gallery.html')
