import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from myapp.models import Client
from django.contrib.auth import authenticate, login as django_login
from myapp.models import User, Category, Product, Manager, Cart, CartLine
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages


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
                # Redirect to index.html
                return redirect('index')
            elif user.role == 'regular_manager':
                request.session['user_id'] = user.id
                # Redirect to managerdashboard.html
                return redirect('managerdashboard')
            elif user.role == 'regular_admin':
                request.session['user_id'] = user.id
                # Redirect to managerdashboard.html
                return redirect('admindashboard')
            else:
                # Handle other roles or scenarios
                pass
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            # Handle invalid credentials
            pass
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

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        api_key = ''
        endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        data = {
            'prompt': user_message,
            'max_tokens': 150
        }
        response = requests.post(endpoint, json=data, headers=headers)
        if response.status_code == 200:
            chatbot_response = response.json()['choices'][0]['text']
            return JsonResponse({'response': chatbot_response})
        else:
            return JsonResponse({'error': 'Failed to get response from OpenAI'}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
    


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
    return redirect('cart')  # Redirect to the cart page after adding to cart



