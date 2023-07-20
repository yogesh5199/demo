from django.contrib import admin
from studentApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','age']
admin.site.register(Student,StudentAdmin)