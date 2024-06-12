from django import forms
from app2.models import students
class InputForm(forms.Form):
    word = forms.CharField(max_length=5, label='Enter a word (3-5 letters)', min_length=3, max_length=5)