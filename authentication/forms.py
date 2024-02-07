from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label="Nom d'utilisateur")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Mot de passe")

User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]
