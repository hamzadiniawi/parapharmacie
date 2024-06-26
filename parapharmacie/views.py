import os
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from myapp.models import Client
from django.contrib.auth import authenticate, login as django_login
from myapp.models import User, Category, Product, Manager, Cart, CartLine, Order, OrderLine, Delivery
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')

def blogDetails(request):
    return render(request, 'blogdetails.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def chatbot(request):
    return render(request, 'chatbot.html')


# @login_required
def cart(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    user_cart = Cart.objects.filter(utilisateur=user)
    cart_lines = CartLine.objects.filter(panier__in=user_cart)
    # Calculate subtotal for each cart line
    for cart_line in cart_lines:
        cart_line.subtotal = cart_line.produit.prix * cart_line.quantite
    total = sum(cart_line.subtotal for cart_line in cart_lines)
    # response = chatbot(request)  # Call the chatbot view
    # chatbot_content = response.content.decode('utf-8')
    return render(request, 'cart.html', {'cart_lines': cart_lines, 'total': total}) #, 'chatbot_content': chatbot_content




def comingsoon(request):
    return render(request, 'comingsoon.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    products = Product.objects.all()
    haircareProducts = Product.objects.filter(categorie__nom='Haircare')
    nutritionalSupplementProducts = Product.objects.filter(categorie__nom='Nutritional Supplement')
    weightManagementProducts = Product.objects.filter(categorie__nom='Weight Management')
    skincareProducts = Product.objects.filter(categorie__nom='Skincare')
    return render(request, 'index.html', {'products': products
                                           , 'haircareProducts': haircareProducts
                                           , 'nutritionalSupplementProducts': nutritionalSupplementProducts
                                           , 'weightManagementProducts': weightManagementProducts
                                           ,'skincareProducts': skincareProducts})

def index2(request):
    products = Product.objects.all()
    haircareProducts = Product.objects.filter(categorie__nom='Haircare')
    nutritionalSupplementProducts = Product.objects.filter(categorie__nom='Nutritional Supplement')
    weightManagementProducts = Product.objects.filter(categorie__nom='Weight Management')
    skincareProducts = Product.objects.filter(categorie__nom='Skincare')
    return render(request, 'index2.html', {'products': products
                                           , 'haircareProducts': haircareProducts
                                           , 'nutritionalSupplementProducts': nutritionalSupplementProducts
                                           , 'weightManagementProducts': weightManagementProducts
                                           ,'skincareProducts': skincareProducts})

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
                request.session['user_id'] = user.id
                return redirect('index')
            elif user.role == 'regular_manager':
                request.session['user_id'] = user.id
                return redirect('managerdashboard')
            elif user.role == 'regular_admin':
                request.session['user_id'] = user.id
                return redirect('admindashboard')
            else:
                # Handle other roles or scenarios
                pass
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')


def logout_user(request):
    # Delete the user_id key from the session
    if 'user_id' in request.session:
        del request.session['user_id']
    # Redirect to the homepage or any other page after logout
    return redirect('login')


def myaccount(request):
    return render(request, 'myaccount.html')

def productdetails(request):
    return render(request, 'productdetails.html')

def shopcollection(request):
    return render(request, 'shopcollection.html')

def shopfullwidth(request):
    return render(request, 'shopfullwidth.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

def shopinstagram(request):
    return render(request, 'shopinstagram.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def managerdashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'managerdashboard.html', {'categories': categories, 'products': products})

def admindashboard(request):
    users = User.objects.all()
    return render(request, 'admindashboard.html', {'users': users})

def add_product(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        image = request.FILES.get('image')
        categorie_id = request.POST.get('categorie')

        product = Product(
            nom=nom,
            description=description,
            prix=prix,
            quantite=quantite,
            image=image,
            categorie_id=categorie_id
        )
        product.save()
        return redirect('managerdashboard')
    return render(request, 'add_product.html')


def add_user(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = User(
            nom=nom,
            prenom=prenom,
            email=email,
            password=password,
            role=role
        )
        user.save()
        return redirect('admindashboard')
    return render(request, 'add_user.html')


def delete_product(request, product_id):
    # Logic to delete the product from the database
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('managerdashboard')

def delete_user(request, user_id):
    # Logic to delete the user from the database
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('admindashboard')


def edit_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        image = request.FILES.get('image')
        categorie_id = request.POST.get('categorie')

        try:
            product = Product.objects.get(pk=id)
            product.nom = nom
            product.description = description
            product.prix = prix
            product.quantite = quantite
            product.categorie_id = categorie_id

            if image:
                product.image = image

            product.save()

            return redirect('managerdashboard')

        except Product.DoesNotExist:
            # Handle the case where the product with the given ID does not exist
            pass
    return redirect('managerdashboard')



def edit_user(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        try:
            user = User.objects.get(pk=id)
            user.nom = nom
            user.prenom = prenom
            user.email = email
            user.password = password
            user.role = role

            user.save()

            return redirect('admindashboard')

        except User.DoesNotExist:
            # Handle the case where the user with the given ID does not exist
            pass
    return redirect('admindashboard')



def chatbotpage(request):
    return render(request, 'chatbotpage.html')

def productdetails(request, product_id):
    # Logic to delete the user from the database
    product = Product.objects.get(pk=product_id)
    return render(request, 'productdetails.html', {'product': product})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(pk=product_id)
            # Retrieve user object using user_id stored in session
            user_id = request.session.get('user_id')
            if user_id:
                user = User.objects.get(pk=user_id)
                cart, created = Cart.objects.get_or_create(utilisateur=user)
                cart_line, created = CartLine.objects.get_or_create(
                    panier=cart,
                    produit=product,
                    defaults={'quantite': 1}
                )
                if not created:
                    cart_line.quantite += 1
                    cart_line.save()
    return redirect('cart')  



@require_POST
def remove_cart_line(request, cart_line_id):
    cart_line = get_object_or_404(CartLine, id=cart_line_id)
    cart_line.delete()
    return redirect('cart')




# @login_required
def place_order(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        user_cart = Cart.objects.filter(utilisateur=user)
        cart_lines = CartLine.objects.filter(panier__in=user_cart)

        # Create the order
        order = Order.objects.create(utilisateur=user, date_commande=timezone.now())

        # Create order lines and remove products from the cart
        for cart_line in cart_lines:
            OrderLine.objects.create(commande=order, produit=cart_line.produit, quantite=cart_line.quantite)
            cart_line.delete()  # Remove the product from the cart

        # Get the address information from the POST data
        region = request.POST.get('region')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        address = f"{region} | {city} | {zip_code}"

        # Create the delivery entry
        Delivery.objects.create(commande=order, adresse=address)

        # Redirect to a thank you page or order summary page
        messages.success(request, 'Order Succeed.')
        return redirect('cart')

    return redirect('cart')  # If not a POST request, redirect to the cart page