from django import forms


class UserLoginForm(forms.Form):
    """ Form To Be Used to log users in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)