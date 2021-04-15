from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.


def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Thank You for registering!')
            form.save()
            return redirect('register')
    else:
        form = RegisterForm()

    context = {
        'form' : form,
    }
    return render(request, 'home/index.html',context)

def gallery(request):
	return render(request, 'home/gallery.html')


