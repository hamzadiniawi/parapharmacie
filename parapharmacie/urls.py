from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blogDetails/', views.blogDetails, name='blogDetails'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('managerdashboard/', views.managerdashboard, name='managerdashboard'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('login/', views.login, name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('productdetails/', views.productdetails, name='productdetails'),
    path('shopcollection/', views.shopcollection, name='shopcollection'),
    path('shopfullwidth/', views.shopfullwidth, name='shopfullwidth'),
    path('shop/', views.shop, name='shop'),
    path('shopinstagram/', views.shopinstagram, name='shopinstagram'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('managerdashboard/', views.managerdashboard, name='managerdashboard'),
]
