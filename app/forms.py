from django.forms import forms

class Login(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.PasswordField(max_length=255)


