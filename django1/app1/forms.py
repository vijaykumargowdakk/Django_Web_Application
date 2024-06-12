from django import forms

class InputForm(forms.Form):
    number = forms.IntegerField(
        label='Enter a number between 1 and 10',
        min_value=1,
        max_value=10
    )