from django.shortcuts import render
from app2.forms import inputform
import itertools

def permute(word):
    return [''.join(p) for p in itertools.permutations(word)]

def home(request):
    permutations = []
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            permutations = permute(word)
            param1 = f"All permutations of {word}:"
            return render(request, 'app4/index.html', {'form': form, 'param1': param1, 'permutations': permutations})
    else:
        form = InputForm()
    return render(request, 'app4/index.html', {'form': form, 'param1': '', 'permutations': permutations})