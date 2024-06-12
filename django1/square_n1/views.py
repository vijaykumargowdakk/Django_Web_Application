from django.shortcuts import render
from .forms import InputForm
import math

def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            square = number ** 2
            factorial = math.factorial(number)
            param1 = f"Square of {number} is {square}, Factorial of {number} is {factorial}"
            return render(request, 'square_n1/index.html', {'form': form, 'param1': param1})
    else:
        form = InputForm()
    return render(request, 'square_n1/index.html', {'form': form, 'param1': ''})
