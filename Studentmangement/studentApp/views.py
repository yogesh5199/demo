from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from studentApp.models import Student
# Create your views here.
class StuListView(ListView):
    model=Student
    template_name='homepage/index.html'
    context_object_name='students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'homepage/form.html'
    fields = ['name', 'rollno','age']
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'homepage/form.html'
    fields = ['name', 'rollno','age' ]
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'homepage/delete.html'
    success_url = reverse_lazy('student_list')
    
