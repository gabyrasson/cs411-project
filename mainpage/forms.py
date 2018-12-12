from django import forms

class SearchForm(forms.Form):
    typein = forms.CharField(label='Search', max_length=100, help_text="Pick either earthquakes, floods, cyclones, or volcanoes.")
