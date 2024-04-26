from django.shortcuts import render

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

def loginregister(request):
    return render(request, 'loginregister.html')

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
