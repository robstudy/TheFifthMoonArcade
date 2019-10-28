from django.shortcuts import render

def user_panel(request):
	return render(request, 'UserPanel/userpanel.html')