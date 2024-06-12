from django.db import models
class students(models.Model):
        fname=models.CharField(max_length=50)
        lname=models.CharField(max_length=100)
        aadhar=models.CharField(max_length=30)
        phone=models.CharField(max_length=30)
        def __str__(self):
                return self.name1

