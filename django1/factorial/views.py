from django.shortcuts import render
from .forms import InputForm
import math

def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            factorial = math.factorial(number)
            return render(request, 'index.html', {'form': form, 'result': f'Factorial of {number} is {factorial}'})
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})
