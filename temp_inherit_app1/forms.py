from  django import forms
class StudentRegistration(forms.Form):  
    First_name=forms.CharField(min_length=5,max_length=30)  
    Last_name=forms.CharField()     
        # label='Myname',label_suffix=':',initial="enter your title",help_text="only last name")
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    agree=forms.BooleanField(label='I agree',label_suffix='')
    rollno=forms.IntegerField(min_value=1)
    
    # stu_pass=forms.CharField(widget=forms.PasswordInput)
    # stu_about_field=forms.CharField(widget=forms.Textarea)
    # stu_check=forms.CharField(widget=forms.CheckboxInput)
    # stu=forms.CharField(widget=forms.FileInput())