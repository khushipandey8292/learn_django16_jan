from  django import forms
class StudentRegistration(forms.Form):
    Last_name=forms.CharField()
    email=forms.EmailField()
    First_name=forms.CharField()   