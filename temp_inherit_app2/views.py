from django.shortcuts import render
from django.http import HttpResponse
from .forms import Studentregister
from .forms import teacherregister
from django.contrib import messages
def course(request):
    
    return render(request,'core1/course_django.html')
# Create your views here.
def make_dynamic_url(request,courseid):
     return HttpResponse(courseid)
 
# def show_details(request,year):
#     return render(request,'pathconverter.html',{'yr':year})

def student_form(request):
    if request.method=='POST':
     fm=Studentregister(request.POST)
     if fm.is_valid():
         fm.save()
    else:
         fm=Studentregister()
    return render(request,'core1/stu_reg.html',{'form':fm})
 
 
def teacher_form(request):
    if request.method=='POST':
     fm=teacherregister(request.POST)
     if fm.is_valid():
         fm.save()
         messages.add_message(request,messages.SUCCESS,'Registration sucessfully!!')
         messages.info(request,"your data is saved!!")
    else:
         fm=teacherregister()
    return render(request,'core1/teach_reg.html',{'form':fm})