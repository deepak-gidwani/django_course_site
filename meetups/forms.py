from django import forms
from .models import *

# class RegisterationForm(forms.ModelForm):
    
#     class Meta:
#         model = Participant
#         fields = ("email",)

class RegisterationForm(forms.Form):
    email = forms.EmailField(label="Your Email")