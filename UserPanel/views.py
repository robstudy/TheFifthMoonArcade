from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from .models import save_user
from django.contrib.auth.decorators import login_required

@login_required
def user_panel(request):
	return render(request, 'UserPanel/userpanel.html')

def register_user(request):
	form = UserRegistrationForm()
	return render(request, 'UserPanel/register.html', {'UserRegistrationForm': form})

def pass_note(request, note):
	form = UserRegistrationForm()
	return render(request, 'UserPanel/register.html', {'UserRegistrationForm': form, 'note': note})

def confirm_registration(request):
	form = UserRegistrationForm()
	user = request.POST.get('username')
	email = request.POST.get('email')
	p1 = request.POST.get('password1')
	p2 = request.POST.get('password2') 
	if p1 != p2:
		return pass_note(request, 'Passwords do not match!')
	saved = save_user(user, email, p1)
	if saved[0]:
		HttpResponseRedirect('accounts/login')
	elif '1062' in saved[1]:
		return pass_note(request, 'Username already in use!')
	else:
		return pass_note(request, saved[1])