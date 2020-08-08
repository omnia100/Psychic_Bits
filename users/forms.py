from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# your_name = forms.CharField(label='Your name', max_length=100)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")