from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=permu(n1)
            return render(request,"app1/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app1/index.html",{'form':form1})

prefix = ""
length = 3
def permu(s, prefix, length):
    if len(prefix) == length:
        print(prefix)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]
            permu(remaining, prefix + s[i], length)