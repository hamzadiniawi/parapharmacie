from django.contrib import admin
from .models import User, Admin, Manager, Client, Actualite, Comment, Product, Category, Stock, Order, OrderLine, Cart, CartLine, Payment, Contact, Delivery
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(User, UserAdmin)

class AdminAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Admin, AdminAdmin)

class ManagerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Manager, ManagerAdmin)

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Client, ClientAdmin)

class ActualiteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Actualite, ActualiteAdmin)

class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Comment, CommentAdmin)

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)

class StockAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Stock, StockAdmin)

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Order, OrderAdmin)

class OrderLineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(OrderLine, OrderLineAdmin)

class CartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Cart, CartAdmin)

class CartLineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(CartLine, CartLineAdmin)

class PaymentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Payment, PaymentAdmin)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Contact, ContactAdmin)

class DeliveryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Delivery, DeliveryAdmin)
