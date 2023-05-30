from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.Textinput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if commit:
            user.save()
        return user
