from django.shortcuts import render
from app2.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app2/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'app2/index.html',{'form':form1})