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
                        'Test Mail', 
                        f"""Dear Student,
Greetings from Entrepreneurship Development Cell, TIET!
We would like to thank you for filling out the registration form and are delighted to announce the start of our flagship event Pitchers 5.0 on 8th November 2020.
Kindly make the registration payment of Rs.100 by any of the following methods:
    1. Using PayTM - Pay to - 8264245458
    2. Using Google Pay - Pay to - 8264245458
    3. Using UPI - Pay to - 8264245458
You must reply to this email with the screenshot of the transaction page to complete your registration. The last date to make the payment is 6th November. If you fail to make the payment by the date mentioned, you will not be allowed to access the dashboard for team formation and your registration will be cancelled.
Join our official discord channel for further updates and news.
Discord link- https://discord.gg/5qeZp9N2SK
Psych yourself up as it’s time to research, ideate and explore the arena of emerging startups.
Good luck.
Regards,
EDC TIET
                        """, 
                        'pitchers@edctiet.com',
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
