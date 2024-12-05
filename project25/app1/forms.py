from django import forms
class RegisterForm(forms.Form):
    name=forms.CharField(label="Name",max_length=20)
    uname=forms.CharField(label="UseName",max_length=20)
    password=forms.CharField(label="password",widget=forms.PasswordInput)