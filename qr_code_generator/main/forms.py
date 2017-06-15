from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class GifForm(forms.Form):
    url = forms.CharField(max_length=100)
    colorful = forms.CharField(max_length=100)
    picture = forms.ImageField()
