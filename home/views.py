from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def programs(request):
    return render(request, 'program.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            message = message
        )
        data.save()

    return render(request, 'contact.html')

def addmarks(request):
    classnames = ClassName.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()
    return render(request, 'addmarks.html', {'classnames' : classnames, 'subjects' : subjects, 'students': students})

def addsubjectmarks(request):
    if request.method == 'POST':
        classnames = ClassName.objects.all()
        subjects = Subject.objects.all()
        students = Student.objects.all()
        obntainedmarks = request.POST['{{subject.name}}']
        data = StudentResult.objects.create(

        )
        return render(request, 'addsubjectmarks.html', {'classnames' : classnames, 'subjects' : subjects, 'students': students})