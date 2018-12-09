from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name',max_length=30)
    email = forms.EmailField(label='Email',max_length=100)
