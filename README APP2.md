# Django Project Creation Procedure Document
## Database tables are created in Django's SQLite



#### >django startproject django12
#### >cd django12
#### >django startapp app1


Add to models.py
```
from django.db import models
class students(models.Model):
        name1=models.CharField(max_length=50)
        college1=models.CharField(max_length=100)
        course1=models.CharField(max_length=30)
```

Create new file forms.py and add
```
from django import forms
from app1.models import students
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']
```

Add to views.py
```
from django.shortcuts import render
from app1.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'app1/index.html',{'form':form1})
```


Add to index.html
```
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Submit</button>
    </form>
    <p>{{param1}}</p>
```


#### >python manage.py makemigrations
#### >python manage.py migrate

#### http://127.0.0.1:8080/app1       
#### >python manage.py createsuperuser   
#### http://127.0.0.1:8080/admin

Add to models.py - so that the object name is the same as the student's name
```
def __str__(self):
        return self.name1
```
        
Add to admin.py
```
from .models import students
admin.site.register(students)
```

We can also check by clicking on db.sqlite
Install SQLite Viewer extension in VSCode

