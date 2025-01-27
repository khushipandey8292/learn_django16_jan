from django.db import models
class Newuser(models.Model):
    id=models.IntegerField(primary_key=True)
    Teach_name=models.CharField(max_length=20)
    stu_name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=4)
# Create your models here.
