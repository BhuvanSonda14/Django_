from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    test=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee_test(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    test=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Final_trial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    test=models.CharField(max_length=50)
    slug=models.SlugField(default="", null=False)

    def __str__(self):
        return self.name

    
