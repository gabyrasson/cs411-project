from django import forms

class SearchForm(forms.Form):
    typein = forms.CharField(label='Search', max_length=100)
