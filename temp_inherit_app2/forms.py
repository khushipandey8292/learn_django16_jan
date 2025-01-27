from django import forms  
from .models import Newuser

class Studentregister(forms.ModelForm):
    class Meta:
        model=Newuser
        fields=['id','stu_name','email','password']
        widgets={'password':forms.PasswordInput}
    
class teacherregister(Studentregister):
    class Meta(Studentregister.Meta):
        fields=['id','Teach_name','email','password']