from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model
import moncashify
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)
     

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)
   

    class Meta:
        ordering = ['-date_added']


    def __str__(self):
        return self.name   
 
 
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=500)
    description = models.TextField()
    date_ajout = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name   

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True) 
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)   

    def __str__(self):
        return str(self.id)  

    @property
    def product_physique(self):
        """ savoir si nous avons au moins un produit physique"""
        articlecommande = self.commandearticle_set.all()
        physique = any(article.product.digital==False for article in articlecommande)
        return physique
        

    @property 
    def get_panier_total(self):
        """ prix total des articles dans le panier"""
        articlecommande = self.commandearticle_set.all()
        total = sum([article.get_total for article in articlecommande])
        return total  

    @property
    def get_panier_article(self):
        """ Nombre total des articles dans le panier"""
        articlecommande = self.commandearticle_set.all()
        quantite_total = sum([article.quantite for article in articlecommande])
        return quantite_total

class CommandeArticle(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantite * self.product.price
        return total


class AddressChipping(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    addresse = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)
    pays = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_ajout =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addresse


    
@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

post_save.connect(create_client, sender=User)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date_ajout = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return f"Message de {self.name}"    

class Laptop(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=500)
    description = models.TextField()
    date_ajout = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name   

class Smartphone(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=500)
    description = models.TextField()
    date_ajout = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name   


class Vehicule(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=500)
    description = models.TextField()
    date_ajout = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.name   
