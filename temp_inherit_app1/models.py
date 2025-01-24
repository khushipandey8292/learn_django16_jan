from django.db import models
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=40)
    stuemail=models.EmailField(max_length=50)
    stupass=models.CharField(max_length=50)
    stubranch=models.CharField(max_length=10,default='not available')

    def __str__(self):
        return self.stuname

class User(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)