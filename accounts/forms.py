from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    """Sign-up form: username, email, password (+ confirm)."""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    """Edit the optional profile fields (bio, avatar, website)."""

    class Meta:
        model = Profile
        fields = ["bio", "avatar", "website"]
