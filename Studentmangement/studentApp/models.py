from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    age=models.IntegerField()

    def __str__(self):
        return self.name
   