#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django import forms

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))  # User cant change the username
    password = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))