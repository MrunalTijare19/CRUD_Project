from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentform

# Create your views here.

class Home(View):
    def get(self,request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html',{'studata':stu_data})

class Add_Student(View):
    def get(sel,request):
        fm = AddStudentform()
        return render(request, 'core/add-student.html',{'form':fm})

def post(sel, request):
    fm = AddStudentform(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
         return render(request, 'core/add-student.html',{'form':fm})


