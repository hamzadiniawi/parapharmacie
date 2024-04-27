from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()

class Admin(User):
    role = models.CharField(max_length=255)

class Manager(User):
    department = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

class Client(User):
    address = models.TextField()
    tel = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    account_creation_date = models.DateField()
    role = models.CharField(max_length=255)

class Actualite(models.Model):
    id_actualite = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    text = models.TextField()

    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produits/')
    categorie = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    attribute = models.CharField(max_length=255)
    publication_date = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    note = models.IntegerField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    produit = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commande = models.DateTimeField()
    statut = models.CharField(max_length=100, default='En attente')

class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    commande = models.ForeignKey(Order, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

class CartLine(models.Model):
    id = models.AutoField(primary_key=True)
    panier = models.ForeignKey(Cart, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    commande = models.OneToOneField(Order, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_reglement = models.DateTimeField()
    mode_paiement = models.CharField(max_length=100)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    commande = models.OneToOneField(Order, on_delete=models.CASCADE)
    adresse = models.TextField()
    date_livraison = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=100, default='En attente')
