from django.shortcuts import render
from temp_inherit_app1.models import Student
def home(request):
    return render(request,'core/home.html')
def about(request):
    return render(request,'core/about.html')
def studentinfo(request):
    stud=Student.objects.all()
    print('Myoutput',stud)
    return render(request,'core/studentdetail.html',{'stu':stud})
# Create your views here.
