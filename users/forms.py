from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cars.models import CommentModel

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']

class ChangeUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
