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
                        f"""Dear Student,
Greetings from EDC TIET!
We hope you’re excited and all prepared for E-Summit 2021. You have successfully subscribed for the enthralling event and we are delighted to have you onboard with us. Brace yourselves for the jam-packed events full of thrill and adventure. Get ready for a breathtaking experience like never before.
Regards,
EDC TIET
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
