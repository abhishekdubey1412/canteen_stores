from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home_App.models import Book_Table
from django.contrib.auth.models import User, auth
import random

# Create your views here.

# function for otp generation
def otp_create():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    return otp


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def order(request):
    return render(request, 'order.html')

def book_table(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')
    
        if name != '' and email != '' and number != '' and date != '' and person != '':
            date = Book_Table(Name=name, Email=email, Number=number, Date=date, Person=person)
            date.save()
            return render(request, 'thanks.html')
        
    return render(request, 'book.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return render(request, 'user_dashboard.html')

    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('rpassword')
        sing_up = request.POST.get('sing_up')

        if password == repeat_password:
            if first_name != '' and last_name != '' and email != '' and username != 'username' and password != '' and repeat_password != '' and sing_up == '1':
                otp = otp_create()
                data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                data.save()
                return redirect('Verification')

    return render(request, 'registration.html')