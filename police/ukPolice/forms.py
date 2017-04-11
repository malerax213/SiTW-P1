#from django import forms

#class LoginForm(forms.Form):
    #name_user = forms.CharField(max_length=20, required=True,Label="",
    #    widget=(forms.TextInput(attrs={"placeholder":"Username","class":"input-login"})))

    #password_user = forms.CharField(max_length=20, required=True,Label="",
    #    widget=(forms.PasswordInput(attrs={"placeholder":"Password","class":"input-login"})))

#class RegisterForm(forms.Form):
#    email_user = forms.CharField(max_length=40, required=True,Label="",
#        widget=(forms.TextInput(attrs={"placeholder":"E-mail","class":"input-register"})))

#    names_user = forms.CharField(max_length=40, required=True,Label="",
#        widget=(forms.TextInput(attrs={"placeholder":"Name","class":"input-register"})))

#    password_user = forms.CharField(max_length=40, required=True,Label="",
#        widget=(forms.TextInput(attrs={"placeholder":"Password","class":"input-register"})))
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
