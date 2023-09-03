from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home_App.models import Book_Table, Employees
from django.contrib.auth.models import User, auth

# Create your views here.

Active_User = False

def home(request):
    data = {
        'title' : 'Canteen Store',
        'active_user' : Active_User
    }
    return render(request, 'home.html', data)

def about(request):
    data = {
        'title' : 'About Us',
        'active_user' : Active_User
    }
    return render(request, 'about.html', data)

def order(request):
    data = {
        'title' : 'Order',
        'active_user' : Active_User
    }
    return render(request, 'order.html', data)

def book_table(request):
    data = {
        'title' : 'Book table',
        'active_user' : Active_User
    }
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
        
    return render(request, 'book.html', data)

def menu(request):
    data = {
        'title' : 'Canteen Menu',
        'active_user' : Active_User
    }
    return render(request, 'menu.html', data)


def login(request):
    global Active_User
    data = {
        'title' : 'User LogIn',
        'is_exist' : False,
        'active_user' : Active_User,
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Employees.objects.filter(Username = username, Password = password).values()
        
        if user.exists():
            Active_User = True
            return redirect('user')
        else:
            data['is_not'] = True
            return render(request, 'login.html', data)

    return render(request, 'login.html', data)


def registration(request):
    data = {
        'title' : 'Registration Page',
        'is_correct' : False,
        'active_user' : Active_User
    }
    
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('rpassword')
        sing_up = request.POST.get('sing_up')

        if password == repeat_password and not Employees.objects.filter(Password = password).values().exists() | Employees.objects.filter(Email=email).values().exists() | Employees.objects.filter(Username=username).values().exists():
            if first_name != '' and last_name != '' and email != '' and username != 'username' and password != '' and repeat_password != '' and sing_up == '1':
                data = Employees(First_Name=first_name, Last_Name=last_name, Email=email, Username=username, Password=password)
                data.save()
                return redirect('login')
        else:
            data['is_correct'] = True
            return render(request, 'registration.html', data)

    return render(request, 'registration.html', data)

def user(request):
    data = {
        'title' : 'User Dashboard',
        'active_user' : Active_User
    }

    return render(request, 'user_dashboard.html', data)