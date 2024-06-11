from django import forms
class inputform(forms.Form):
    input1=forms.CharField(min_length=1,max_length=10,label="enter your word")