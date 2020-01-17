from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": f"form-control", 'placeholder': 'Enter your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Enter your email address"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Enter your content"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("email must be gmail.com")
        return email


# login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=20)


# registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=20)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(), max_length=20)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email alerady taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password2 != password:
            raise forms.ValidationError("passwords didn't match")
        return data
