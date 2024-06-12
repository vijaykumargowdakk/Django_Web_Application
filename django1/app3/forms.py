from django import forms
from app3.models import students
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['fname','lname','aadhar','phone']