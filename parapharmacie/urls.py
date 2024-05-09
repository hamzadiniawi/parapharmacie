from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blogDetails/', views.blogDetails, name='blogDetails'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
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
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit_user/', views.edit_user, name='edit_user'),



] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)