from django.contrib import admin
from temp_inherit_app1.models import Student
from .models import User
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass','stubranch')
    

# admin.site.register(Student,StudentAdmin)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
    
# admin.site.register(User1,User1Admin)