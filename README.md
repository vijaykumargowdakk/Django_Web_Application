# Django_Procedure

*How to add multiple apps in a single project.*   
*Here are the steps to follow :-*

## PHASE1: Project creation 
**Step1 :** In Terminal  
```
django-admin startproject django1
```
It is used to create a project with *folder name* and *project name* as **django1**  

**Step2 :** 
```
cd django1
```
We changed the current dirctory to *django1*  

**Step3 :** 
```
django-admin startapp app1  
```
We created an app with *app name* as **app1**  

**Step4 :** 
Within Django1 project, we can create multiple apps. Let us name them as app1, app2, app3. The browser home page for each of these apps will be 
http://127.0.0.1:8000/app1   

http://127.0.0.1:8000/app2   

http://127.0.0.1:8000/app3   

http://127.0.0.1:8000/admin - commmon admin control for all the apps   


## PHASE2: Creating urls 
**Step5 :**  
5a) In app1, create folder templates  
5b) In app1/templates, create folder app1   
5c) In app1/templates/app1, create file index.html  
  
**Step6:**  In index.html write a program which include 'Hello World' and {{param1}}  
```
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
```

**Step7 :** Go to django1/settings.py add 
```
INSTALLED_APPS = [...,"app1", ]
```

**Step8 :** Go to app1/views.py
```
def home(request):
    return render(request,'app1/index.html',{'param1':"hello world"})
```

**Step9 :** Create urls.py in app1 and add
```
from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]
```
This is not mandatory to create urls.py for each apps. you can add all apps path in urls.py in main project.  
It's an option that most Django developer seem to take advantage of because it helps keep your code organized - i,e; the urls relevant to a specific app live in that app's folder.  

**Step10 :** In django1/urls.py  
There will be  two parts :  
10a) After ```from django.urls import path```  
import include- It is used for including the content of a file into your current program.  
```
from django.urls import include
```
10b) Inside urlpatterns  add
```
path("app1/" ,include("app1.urls")),
```

**Step11 :** In Terminal run,  
```
python manage.py runserver
```  
You will get output as   
Hello World   
hello world  
In Browser,
We should make changes in the server at localhost port 8000 i.e; **127.0.0.1:8000/app1**


## PHASE3: Logic to be implemented in views.py for taking input from a HTML Form
**Step12 :**
Something like this  
```
from django.shortcuts import render
def home(request):
    factorial=1
    n1=5
    for i in range(1,n1+1,1):
        factorial=factorial*i
    return render(request,'app1/index.html',{'param1':factorial,'param2':n1})

```
Also make changes in index.html  
```
<body>
    <p>Hello World</p>
    <p>The factorial of {{param1}} is {{param2}}</p>
</body>
```  
We should get output as *The factorial of 5 is 120*  

## PHASE4: add forms to take input from the user ##
 We can modify the code using forms  
 **Step13 :** create forms.py in the factorial1 folder  
```
from django import forms
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=1,max_value=10,label="Enter a number")
```

**Step14 :** in index.html
```
<body>
    <h1>Factorial Program</h1>
    <form method="POST">
    {% csrf_token %}
    {{form.as_p}}    
    <button type="submit">find factorial</button>
    </form>
    {% if param1 %}
    <h2>Factorial of {{param2}} is {{param1}}</h2>
    {% endif %}
</body>
```
*we can use (p, ul, table)  where  p-paragraph, ul-unordered list, table-table*  
   
**Step15 :** in app1/views.py, 
```
from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=fact(n1)
            return render(request,"factorial1/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"factorial1/index.html",{'param1':result, 'param2':n1, 'form':form1})
```
```
def fact(n1):  
    result=1
    for i in range(1,n1+1,1):
        result=result*i
    return result
```
```
>python manage.py runserver
```
http://127.0.0.1:8000/app1                              
----End of Factorial Program in App1--------------  

Assignment: Create app2 to print factorial numbers from 1 to 8, one below the other as shown. Let us return param1=[1,2,6,24,120,720,5040,40320] and param2=[1,2,3,4,5,6,7,8] from views.py and iterate these 2 lists using {% for each %} syntax  
    

Factorial of 1 - 1   
Factorial of 2 - 2   
Factorial of 3 - 6   
Factorial of 4 - 24   
Factorial of 5 - 120   
Factorial of 6 - 720   
Factorial of 7 - 5040   
Factorial of 8 - 40320

Changes in the body section of index.html
```  
<body>   
  <p>Factorial of Numbers</p>
  {% for i in param1 %}
  <p>{{i}}</p>
  {% endfor %}   
</body>
``` 


We can further enhance the index.html 
```


<body>   
  <p>Factorial of Numbers</p>
  {% for i,j in param1 %}
  <p>Factorial of {{j}} - {{i}}</p>
  {% endfor %}   
</body>

```
Corresponding changes in views.py
```
def home(request):
    result=getFact(8)
    return render(request,'app2/index.html',{'param1':result})

def getFact(limit):
    factorial=[]
    numbers=[]
    for j in range(1,limit+1,1):
        n1=j
        fact1=1
        for i in range(1,n1+1,1):
            fact1=fact1*i
        factorial.append(fact1)
        numbers.append(n1)
    return zip(factorial,numbers)
```
   



## Basic Setup for new programmers

1. Testing for sample Python projects, 1.py to 16.py.  We recommend the use of IDLE for building simple Python code.  During installation, please tick the box - Add Path -  This is very important
https://www.python.org/


2. Django installation.  Go to IDLE - File - Path Browser. Check the location where Python is installed. Eg
>cd USERS
>
>cd LAPTOP
>
>cd AppData  ( This is a hidden folder, but we can go to cmd and change directory)
>
> cd Local
>
> cd Programs
>
> cd Python
>
> cd Python312
>
> cd Scripts
>
> pip3 install django
>
> pip3 install mysql-connector-python
>

3. MySQL installation.  Choose MySQL Community (GPL) Downloads and install 2 products
   
a) MySQL Server   

b) MySQL Workbench   

set username=root,  password=root   

### >create database db1
### >create table employee(id bigint auto_increment primary key, name1 varchar(100))
### >insert into employee(name1) values ("Chandra"), ("Siva"), ("Rajani")
### >select * from employee
https://www.mysql.com/downloads/   

4. VS Code Installation
https://code.visualstudio.com/download
Add extension for Python (Python language support) from Microsoft

5. Git, GitHub 
- Download Git for Windows https://git-scm.com/download/win   Carefully complete the elaborate installation procedure consisting of about 10 steps
- Create account in https://github.com/

6. Basic Testing of all Components
- Choose a working directory D:\coding
- Create a sub-directory:  \django.   
So, all your work will be in D:\coding\django  (preferred) OR C:\coding\django

In IDLE
File - New File - 
```
print(8+4)
```
 - save as 1.py in D:\coding\django   Run - Run Module

In VS Code
Open folder D:\coding\django\
Create index.html, type ! and Enter.  You will see a predefined HTML code. Run - Run without Debugging - Chrome 
Create 2.py - 
```
print(8+3) 
```
- save as 2.py in D:\coding\django. Open Terminal (... in top line), New Terminal
> python 2.py

7. If python command is not in the path, set the environment variable by typing env, edit system environment variables, go to Path, edit, add New,  copy the directory path where Python is installed, save.  Close cmd or Terminal. Open again cmd or Terminal.


8. If django-admin command is not in the path, set the environment variable by typing env, edit system environment variables, go to Path, edit, add New,  copy the directory path where Django is installed, save.  Close cmd or Terminal. Open again cmd or Terminal.

To test, 
>python --version
>django-admin


9. Sample Django programs available in  https://github.com/vijaykumargowdakk/Django_workshop/tree/main

10. Setup procedures in  README.md and README2.md

https://github.com/vijaykumargowdakk/Django_workshop/blob/main/README%20APP2.md

11. An automated program sangamone-django3.0.py to change the following files has been created to change the following files as required by Django
>django1\settings.py
>django1\urls.py
>app1\views.py
>app1\urls.py  (new file to be created)
> templates\app1\index.html  (new file to be created within templates folder and within app1 folder)


