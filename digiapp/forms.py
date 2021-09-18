from django import forms

class RegisterationForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
    confirm_password=forms.CharField(max_length=200)
class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
