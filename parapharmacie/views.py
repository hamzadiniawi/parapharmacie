from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from myapp.models import Client
from django.contrib.auth import authenticate, login as django_login
from myapp.models import User
from myapp.models import Manager


# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')

def blogDetails(request):
    return render(request, 'blogdetails.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def comingsoon(request):
    return render(request, 'comingsoon.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('user-name')
        password = request.POST.get('user-password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        # address = request.POST.get('address')

        # Create a new client object
        client = Client.objects.create(
            nom=username,
            password=password,
            email=email,
            tel=phone_number,
            # address=address,
            username=username,
            account_creation_date=timezone.now(),
            role='regular'  # Default role is set to 'regular'
        )

        # Save the client object
        client.save()

        # Redirect to a success page or any other page after successful registration
        return HttpResponseRedirect('/index/')  # Change this to your desired URL
    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            if user.role == 'regular':
                # Redirect to index.html
                return redirect('index')
            elif user.role == 'regular_manager':
                # Redirect to managerdashboard.html
                return redirect('managerdashboard')
            else:
                # Handle other roles or scenarios
                pass
        except User.DoesNotExist:
            # Handle invalid credentials
            pass
    return render(request, 'login.html')


def myaccount(request):
    return render(request, 'myaccount.html')

def productdetails(request):
    return render(request, 'productdetails.html')

def shopcollection(request):
    return render(request, 'shopcollection.html')

def shopfullwidth(request):
    return render(request, 'shopfullwidth.html')

def shop(request):
    return render(request, 'shop.html')

def shopinstagram(request):
    return render(request, 'shopinstagram.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def managerdashboard(request):
    return render(request, 'managerdashboard.html')
