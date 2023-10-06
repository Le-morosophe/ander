from django.contrib import admin
from .models import *

class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'digital', 'image', 'date_ajout')    

class CommandeModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'complete', 'status', 'total_trans', 'transaction_id', 'date_commande')    

class CommandeArticleModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'commande', 'quantite', 'date_added')  

class AddressChippingModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'commande', 'addresse', 'ville', 'zipcode', 'date_ajout')      

class VehiculeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'date_ajout', 'image', 'description') 

class SmartphoneModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'date_ajout', 'image', 'description')  

class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'date_ajout', 'image', 'description') 

class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_ajout')
    


admin.site.register(Client, ClientModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Commande, CommandeModelAdmin)
admin.site.register(CommandeArticle, CommandeArticleModelAdmin)
admin.site.register(AddressChipping, AddressChippingModelAdmin)
admin.site.register(Vehicule, VehiculeModelAdmin)
admin.site.register(Laptop, LaptopModelAdmin)
admin.site.register(Smartphone, SmartphoneModelAdmin)
admin.site.register(Message, MessageModelAdmin)

admin.site.site_title = "Django Ecom"
admin.site.site_header = "Django Ecom"
admin.site.index_title = "DJango Ecom"