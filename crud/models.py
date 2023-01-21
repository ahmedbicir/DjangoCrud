from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=100, unique=True)
    course = models.CharField(max_length=100)
    nationalId = models.CharField(max_length=100)
    date_reg = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=100, default=None, null=True)
    mode = models.CharField(max_length=100, null=True, blank=True)
    languages = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

    # signup model


class Signup(models.Model):
    studentname = models.CharField(max_length=100)
    regno = models.CharField(max_length=100, unique=True)
   

    def __str__(self):
        return self.studentname