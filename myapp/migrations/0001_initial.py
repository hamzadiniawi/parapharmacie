# Generated by Django 5.0.4 on 2024-04-27 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id_actualite', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('role', models.CharField(max_length=255)),
            ],
            bases=('myapp.user',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('address', models.TextField()),
                ('tel', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('account_creation_date', models.DateField()),
                ('role', models.CharField(max_length=255)),
            ],
            bases=('myapp.user',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('department', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
            ],
            bases=('myapp.user',),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_commande', models.DateTimeField()),
                ('statut', models.CharField(default='En attente', max_length=100)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adresse', models.TextField()),
                ('date_livraison', models.DateTimeField(blank=True, null=True)),
                ('statut', models.CharField(default='En attente', max_length=100)),
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_reglement', models.DateTimeField()),
                ('mode_paiement', models.CharField(max_length=100)),
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='produits/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('produit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('attribute', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('note', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
        ),
    ]
