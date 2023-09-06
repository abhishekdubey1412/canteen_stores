from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home_App.models import Book_Table, Employees, Items, CardItems
from django.contrib.auth.models import User, auth
import random
import datetime

# Create your views here.

Active_User = False
query_data = Items.objects.all()
ItemsOfDay_1 = random.choice(query_data)
ItemsOfDay_2 = random.choice(query_data)

if ItemsOfDay_1 == ItemsOfDay_2:
    ItemsOfDay_2 = random.choice(query_data)

# Get the current date
current_date = datetime.datetime.now()

# Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = current_date.weekday()

# Define a list of day names
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
name_of_day = day_names[day_of_week]

def home(request):
    data = {
        'title' : 'Canteen Store',
        'active_user' : Active_User
    }

    return render(request, 'home.html', {'data': data, 'query_data': query_data, 'ItemsOfDay_1': ItemsOfDay_1, 'ItemsOfDay_2': ItemsOfDay_2, 'name_of_day': name_of_day })

def about(request):
    data = {
        'title' : 'About Us',
        'active_user' : Active_User
    }
    return render(request, 'about.html', {'data': data})

def order(request):
    data = {
        'title' : 'Order',
        'active_user' : Active_User
    }
    return render(request, 'order.html', {'data': data})

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
        
    return render(request, 'book.html', {'data': data})

order_item = False

def add_data(order_item):
    if order_item:
        user_id = order_item
        item_image  = Items.objects.get(id=order_item).Image
        item_name = Items.objects.get(id=order_item).Title
        item_type = Items.objects.get(id=order_item).Type
        item_price = Items.objects.get(id=order_item).Price
        card_data = CardItems(Image=item_image, Name=item_name, Type=item_type, Price=item_price, UserId=user_id)
        card_data.save()

def menu(request):
    global order_item
    data = {
        'title' : 'Canteen Menu',
        'active_user' : Active_User
    }

    query_data = Items.objects.all()

    if request.method == "POST":
        active = request.POST.get('show_svg')

        if active == "not_active":
            return redirect('login')
        elif active:
            order_item = active
    
        add_data(order_item)
        
    return render(request, 'menu.html', {'data': data, 'query_data': query_data})


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
            return render(request, 'login.html', {'data': data})

    return render(request, 'login.html', {'data': data})


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
            return render(request, 'registration.html', {'data': data})

    return render(request, 'registration.html', {'data': data})

def user(request):
    global Active_User
    data = {
        'title' : 'User Dashboard',
        'active_user' : Active_User
    }

    if request.method == "POST":
        sing_out = request.POST.get('sing_out')

        if sing_out == '1':
            Active_User = False
            return redirect('login')

    return render(request, 'user_dashboard.html', {'data': data})

def card(request):
    data = {
        'title' : 'Shopping Card',
        'active_user' : Active_User,
    }
    
    DataOfCard = CardItems.objects.all()

    return render(request, 'shopping_cart.html', {'data': data, 'DataOfCard': DataOfCard})