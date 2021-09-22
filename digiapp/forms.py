from django import forms
from django.db.models.base import Model
from django.forms.models import ModelForm
from digiapp.models import Review
class RegisterationForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
    confirm_password=forms.CharField(max_length=200)
class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
class ReviewForm(forms.Form):
    review_text=forms.CharField(max_length=1000)
    score=forms.IntegerField(min_value=1,max_value=5)