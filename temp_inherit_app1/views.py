from django.shortcuts import render
from temp_inherit_app1.models import Student
from .forms import StudentRegistration
from django.contrib.auth.models import User
def home(request):
    return render(request,'core/home.html')
def about(request):
    return render(request,'core/about.html')

def studentinfo(request):
    stud=Student.objects.all()
    print('Myoutput',stud)
    return render(request,'core/studentdetail.html',{'stu':stud})
 
def showformdata(request):
 fm=StudentRegistration(auto_id=True,label_suffix='-')
 fm.order_fields(field_order=['First_name','Last_name','email'])
 return render(request,'core/studentform.html',{'form':fm})
