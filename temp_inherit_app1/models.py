from django.db import models
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=40)
    stuemail=models.EmailField(max_length=50)
    stupass=models.CharField(max_length=50)
# Create your models here.
