from django.contrib import admin
from temp_inherit_app1.models import Student

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass','stubranch')
    

admin.site.register(Student,StudentAdmin)
# Register your models here.
