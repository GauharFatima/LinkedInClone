from django import forms
from AccountsApp.models import MyUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'


class LogInForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'password']
