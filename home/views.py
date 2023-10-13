from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

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
        if len('name') >= 20:
            messages.error(request, 'Please enter a valid name')
        else:
            data = Contact.objects.create(
                name = name,
                email = email,
                phone = phone,
                message = message
            )
            data.save()
            message = {'message' :'Your message is submitted successfully'}
            return render(request, 'contact.html', message)

        data.save()
        message = {'message': 'Your message is submitted successfully'}
        return render(request, 'contact.html', message)

    return render(request, 'contact.html')

def addmarks(request):
    classnames = ClassName.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()
    return render(request, 'addmarks.html', {'classnames' : classnames, 'subjects' : subjects, 'students': students})

def addsubjectmarks(request):
    classnames = ClassName.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()

    return render(request, 'addsubjectmarks.html', {'classnames' : classnames, 'subjects' : subjects, 'students': students})

def viewresult(request):
    students = Student.objects.all();
    return render(request, 'viewresult.html', {'students': students})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already taken')
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                data.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, 'Password does not match !')
            return redirect('/signup')

    return render(request, 'signup.html')

# def login(request):
#     return render(request, 'registration/login.html')