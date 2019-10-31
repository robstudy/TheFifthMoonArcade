from django.db import models
from django.contrib.auth.models import User

def save_user(user_name, email, password):
	try:
		user = User.objects.create_user(user_name, email, password)
		user.save()
		return (True, '')
	except Exception as e:
		return (False, str(e))


