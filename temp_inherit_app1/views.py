from django.shortcuts import render
from temp_inherit_app1.models import Student
from  temp_inherit_app1.models import User
from .forms import StudentRegistration
# from django.http import HttpResponseRedirect
def home(request):
    return render(request,'core/home.html')
def about(request):
    return render(request,'core/about.html')

def studentinfo(request):
    stud=Student.objects.all()
    print('Myoutput',stud)
    return render(request,'core/studentdetail.html',{'stu':stud})
 
# def showformdata(request):    
#  fm=StudentRegistration(auto_id=True,label_suffix='-')
#  fm.order_fields(field_order=['First_name','Last_name','email'])
#  return render(request,'core/studentform.html',{'form':fm})

# def thanyou(request):
#     return render(request,'core/success.html')

# def showformdata(request):
#     if request.method=='POST':
#         fm=StudentRegistration(request.POST)
#         if fm.is_valid():
#             print("Form validated..")
#             print('F_Name:',fm.cleaned_data['First_name'])
#             print('L_Name:',fm.cleaned_data['Last_name'])
#             print('Email:',fm.cleaned_data['email']) 
#             print('Password:',fm.cleaned_data['password'])
#             print('agree:',fm.cleaned_data['agree'])
#             print('Rollno:',fm.cleaned_data['rollno'])
#             return HttpResponseRedirect('/temp_app1/success/')
#             # return render(request,'core/success.html/')    
#     else:
#         fm=StudentRegistration()
#     return render(request,'core/studentform.html',{'form':fm})


# def showformdata(request):
#     if request.method=='POST':
#         fm=StudentRegistration(request.POST)
#         if fm.is_valid():
#             print("Form validated..")
#             print('Name:',fm.cleaned_data['name'])
#             print('Email:',fm.cleaned_data['email']) 
#             print('Password:',fm.cleaned_data['password'])
#             return HttpResponseRedirect('/temp_app1/success/')
#             # return render(request,'core/success.html/')    
#     else:
#         fm=StudentRegistration()
#     return render(request,'core/studentform.html',{'form':fm})



def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form validated..")
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email']) 
            print('password:',fm.cleaned_data['password'])
            print('Rpassword:',fm.cleaned_data['Rpassword'])   
    else:
        fm=StudentRegistration()
    return render(request,'core/studentform.html',{'form':fm})



def showformdata(request):
    if request.method=='POST':
        pi=User.objects.get(pk=1)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
        #    nm=fm.cleaned_data['name']
        #    em=fm.cleaned_data['email']
        #    pm=fm.cleaned_data['password']
        #    reg=User(name=nm,email=em,password=pm)
        #    reg.save()  
        #    print(nm)
        #    print(em)
        #    print(pm)
             fm.save()
    else:
        fm=StudentRegistration()
    return render(request,'core/studentform.html',{'form':fm})

    
    