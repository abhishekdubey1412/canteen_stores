from django.db import models

# Create your models here.
class Book_Table(models.Model):
    Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55)
    Number = models.IntegerField()
    Date = models.DateField()
    Person = models.IntegerField() 

class Employees(models.Model):
    First_Name = models.CharField(max_length=55)
    Last_Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55)
    Username = models.CharField(max_length=55)
    Password = models.CharField(max_length=55)