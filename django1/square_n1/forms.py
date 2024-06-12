from django import forms
from square_n1.models import square_n1
from django import forms

class InputForm(forms.Form):
    number = forms.IntegerField(widget=forms.HiddenInput(), initial=5)
