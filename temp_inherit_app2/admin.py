from django.contrib import admin
from .models import Newuser
@admin.register(Newuser)
class NewuserAdmin(admin.ModelAdmin):
   list_display=['id','stu_name','Teach_name','email','password']
# Register your models here.
