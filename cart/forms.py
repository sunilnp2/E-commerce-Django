# from logging import PlaceHolder
# from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
# from django.contrib.auth.models import User
# from django.core import validators
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from .models import *

# def checkdigit(value):
#     if value.isdigit() == False:
#         raise forms.ValidationError("You can contain only digit")
#     if len(value) != 10:
#         raise forms.ValidationError("Phone Lengh Must be 10")

# class BillAddress(forms.Form):
#     name = forms.CharField(label = "Full Name:",
#     error_messages={'request':"This field is required"},
#     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Full Name'}))

#     phone = forms.ImageField(label = "Enter Phone:",validators= [checkdigit],
#     error_messages={'request':"This field is required"},
#     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Phone'}))

#     address = forms.CharField(label = "Address:",
#     error_messages={'request':"This field is required"},
#     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter address '}))