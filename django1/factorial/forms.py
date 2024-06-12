from django import forms
from app3.models import factorial

class InputForm(forms.Form):
    number = forms.IntegerField(min_value=1, max_value=10, label='Enter a number (1-10)')
