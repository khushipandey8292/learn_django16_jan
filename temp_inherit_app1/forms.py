from  django import forms
from .models import User

# class StudentRegistration(forms.Form):  
#     First_name=forms.CharField(min_length=5,max_length=30)  
#     Last_name=forms.CharField()     
#         # label='Myname',label_suffix=':',initial="enter your title",help_text="only last name")
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     agree=forms.BooleanField(label='I agree',label_suffix='')
#     rollno=forms.IntegerField(min_value=1)
    
    # stu_pass=forms.CharField(widget=forms.PasswordInput)
    # stu_about_field=forms.CharField(widget=forms.Textarea)
    # stu_check=forms.CharField(widget=forms.CheckboxInput)
    # stu=forms.CharField(widget=forms.FileInput())
    
    
# cleaning and validating specific field with the help of method...

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super().clean()
        valname = self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        if len(valname)<4:
            raise forms.ValidationError('enter name more then or equal to 4 char')
        # return valname

        # validation of complete django form at once  

        if len(valemail)<10:
            raise forms.ValidationError('email should be more than 10 or equal to 10')



class StudentRegistration(forms.Form):
    name=forms.CharField(error_messages={'required':'enter your name'})
    email=forms.EmailField(error_messages={'required':'enter your email'})
    password=forms.CharField(widget=forms.PasswordInput(),error_messages={'required':'enter your password'})
    Rpassword=forms.CharField(label='password(again)',widget=forms.PasswordInput(),error_messages={'required':'please re-enter your password'})
    
    
class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    Rpassword=forms.CharField(label='password(again)',widget=forms.PasswordInput()) 
    def clean(self):
        cleaned_data=super().clean()
        valpass=self.cleaned_data['password']
        valrpass=self.cleaned_data['Rpassword']
        if valpass!=valrpass:
            raise forms.ValidationError('password does not match')



class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'enter name','email':'enter email','password':'enter password'}
        widgets={'password':forms.PasswordInput}