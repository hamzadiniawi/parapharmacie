from django.contrib import admin
from .models import User, Admin, Manager, Client, Actualite, Comment, Product, Category, Stock, Order, OrderLine, Cart, CartLine, Payment, Contact, Delivery

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Manager)
admin.site.register(Client)
admin.site.register(Actualite)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Cart)
admin.site.register(CartLine)
admin.site.register(Payment)
admin.site.register(Contact)
admin.site.register(Delivery)
