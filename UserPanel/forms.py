#Create user
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',)