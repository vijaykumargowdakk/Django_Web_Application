from django.shortcuts import render
from app1.forms import InputForm
import math

def home(request):
    result = None
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            factorial = math.factorial(number)
            result = f"The factorial of {number} is {factorial}"
            return render(request, 'app1/index.html', {'form': form, 'result': result})
    else:
        form = InputForm()
    return render(request, 'app1/index.html', {'form': form, 'result': result})
