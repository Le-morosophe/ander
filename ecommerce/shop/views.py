
from django.urls import reverse
from collections import UserDict, UserList, UserString
from datetime import datetime
from debugpy.common.util import force_bytes
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from requests import request
from .models import Product, Commande
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from ecommerce.ecommerce import settings
from django.contrib.auth.views import PasswordResetView
from .utils import send_email_with_html_body
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.urls.exceptions import NoReverseMatch
from django.contrib.auth import get_user_model
import json
from .utile import commandeAnonyme, data_cookie, panier_cookie
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Laptop, Smartphone, Vehicule, Message
from .forms import ContactForm


def laptops(request):
    laptops = Laptop.objects.all()
    context = {'laptops': laptops}
    return render(request, 'shop/laptops.html', context)

def smartphones(request):
    smartphones = Smartphone.objects.all()
    data = data_cookie(request)
    nombre_article = data['nombre_article']
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        smartphones = Smartphone.objects.filter(name__icontains=item_name)
    paginator = Paginator(smartphones, 8)
    page = request.GET.get('page')
    smartphones = paginator.get_page(page)
    context = {'smartphones': smartphones, 'nombre_article': nombre_article}
    return render(request, 'shop/smartphones.html', context)

def vehicules(request):
    vehicules = Vehicule.objects.all()
    context = {'vehicules': vehicules}
    return render(request, 'shop/vehicules.html', context)

@login_required
def mon_compte(request):
    return render(request, 'shop/mon_compte.html')

def contact_success(request):
    return render(request, 'shop/contact_success.html')

def contact_form_submit(request):
    if request.method == 'POST':
           name = request.POST['name']
           email = request.POST['email']
           message = request.POST['message']
           msg = Message(name=name, email=email, message=message)
           msg.save()
           return render(request, 'shop/contact_success.html')
    else:
           return render(request, 'shop/contact.html')

def aide(request):
    return render(request, 'shop/aide.html')

def qui_sommes_nous(request):
    return render(request, 'shop/qui_sommes_nous.html')

def contact(request):
    return render(request, 'shop/contact.html')

def terms_conditions(request):
    return render(request, 'shop/terms_conditions.html')


def category_products(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    context = {
        'products': products
    }
    return render(request, 'shop/category_products.html', context)


def index(request):
    product_object = Product.objects.all()
    data = data_cookie(request)
    nombre_article = data['nombre_article']
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(name__icontains=item_name)
    paginator = Paginator(product_object, 8)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    context = {

        'product_object': product_object,
        'nombre_article': nombre_article
    }

    return render(request, 'shop/index.html',  context)

@login_required
def panier(request, *args, **kwargs):
    """ panier """
    
    data = data_cookie(request)
    articles = data['articles']
    commande = data['commande']
    nombre_article = data['nombre_article']

    context = {
        'articles':articles,
        'commande':commande,
        'nombre_article':nombre_article
    }

    return render(request, 'shop/panier.html', context)


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    context = {
        'product': product_object
    }
    return render(request, 'shop/detail.html',context) 


def update_article(request, *args, **kwargs):

    data = json.loads(request.body)

    product_id = data['product_id']

    action = data['action']

    client = request.user.client

    product = Product.objects.get(id=product_id)

    commande, created = Commande.objects.get_or_create(client=client, complete=False)

    commande_article, created = CommandeArticle.objects.get_or_create(commande=commande, product=product)

    if action == 'add':

        commande_article.quantite += 1

    if action == 'remove':

        commande_article.quantite -= 1

    commande_article.save()

    if  commande_article.quantite <= 0:

        commande_article.delete()        

    return JsonResponse("Article ajouté", safe=False)



def traitementCommande(request, *args, **kwargs):
    """ traitement,  validation de la com;ande  et verification de l'integrite des donnees(detection de fraude)"""

    STATUS_TRANSACTION = ['ACCEPTED', 'COMPLETED', 'SUCESS']
    
    transaction_id = datetime.now().timestamp()

    data = json.loads(request.body)

    print(data)

    if request.user.is_authenticated:

        client = request.user.client

        commande, created = Commande.objects.get_or_create(client=client, complete=False)


    else:
        client, commande = commandeAnonyme(request, data)

    total = float(data['form']['total'])

    commande.transaction_id = data['payment_info']['transaction_id']

    commande.total_trans = total

    if commande.get_panier_total() == total:

        commande.complete = True
        commande.status = data['payment_info']['status']

    else:
        commande.status = "REFUSED"
        commande.save()
        
        return JsonResponse("Attention!!! Traitement Refuse Fraude detecte!", safe=False)

    commande.save()    
    
    if not commande.status in STATUS_TRANSACTION:
        return JsonResponse("Désolé, le paiement a échoué, veuillez réessayer")    

  

    if commande.product_physique:

        AddressChipping.objects.create(
            client=client,
            commande=commande,
            addresse = data['shipping']['address'],
            ville=data['shipping']['city'],
            zipcode=data['shipping']['zipcode']
        )


    return JsonResponse("Votre paiement a été effectué avec succès, vous recevrez votre commande dans un instant !", safe=False)


@login_required
def vos_commandes(request):
    # Récupérer les commandes des clients
    commandes = Commande.objects.filter(client=request.user.client)
    
    context = {
        'commandes': commandes
    }
    
    return render(request, 'shop/vos_commandes.html', context)


def commande(request, *args, **kwargs):
    data = data_cookie(request)
    articles = data['articles']
    commande = data['commande']
    nombre_article = data['nombre_article']

    context = {
        'articles':articles,
        'commande':commande,
        'nombre_article': nombre_article
    }

    return render(request, 'shop/commande.html', context)     



def register(request, *args, **kwargs):
    context= {}
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST.get('email')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request, 'ce nom à été déjà pris')
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request, 'cet mail à été déjà pris')
            return redirect('register')
        if not username.isalnum():
            messages.error(request, 'Le nom doit être alphanumérique')
            return redirect('register')
        if password1 != password2:
            messages.error(request, 'Les mots de passe ne sont pas identiques.')
            return redirect('register')
        mon_utilisateur = User.objects.create_user(username, email, password1)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname
        mon_utilisateur.is_active = False
        mon_utilisateur.save()
        
        messages.success(request, 'Votre compte a été crée avec succès. On a envoyée un mail de confirmation, veillez verifier votre mail ')
        uidb64 = urlsafe_base64_encode(force_bytes(mon_utilisateur.pk))
        token = default_token_generator.make_token(mon_utilisateur)
        confirm_url = request.build_absolute_uri(reverse('confirm_account', kwargs={'uidb64': uidb64, 'token': token}))
       
        context = {
            'confirm_url': confirm_url,
        
        }
        email_body = render_to_string('shop/confirmation_email.html', context)
        # Envoyez l'e-mail de confirmation
        send_mail(
            'Confirmation de compte',
            email_body,
            'louisjeananderson2016@gmial.com',
            [mon_utilisateur.email],
            fail_silently=False,
        )
        return redirect('login')
    

    return render(request, 'shop/register.html', context)

def confirm_account(request, uidb64, token):
    # Décodez l'ID de l'utilisateur à partir de l'encodage base64
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        return redirect('confirm_account_failed')
    # Vérifiez si le jeton est valide
    if default_token_generator.check_token(user, token):
        # Activez le compte de l'utilisateur
        user.is_active = True
        user.save()
        return redirect('confirm_account_success')  # Rediriger vers une page de confirmation réussie
    else:
        return redirect('confirm_account_failed')  # Rediriger vers une page d'échec de confirmation
    
def confirm_account_success(request):
    return render(request, 'shop/confirm_account_success.html')

def confirm_account_failed(request):
    return render(request, 'shop/confirm_account_failed.html')


def logi(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']   
        remember_me = request.POST.get('remember_me') 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            if remember_me:
                request.session.set_expiry(604800)  
            else:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, 'Identifiants non valid')
            return redirect('login')
    
    return render(request, 'shop/login.html')

def logOut(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté')   
    return redirect('home')

class MyPasswordResetView(PasswordResetView):
    template_name = 'shop/password_reset.html'
    success_url = reverse_lazy('password_reset_done')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            uid = urlsafe_base64_encode(force_bytes(user.pk, encoding='utf-8'))
            token = default_token_generator.make_token(user)
            
            reset_url = self.request.build_absolute_uri( 
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}) 
            ) 
            
            context = {
                'reset_url': reset_url,
                'uidb64': uid,
                'token': token,
            }
            subject = 'Email de réinitialisation de mot de passe'
            email_template_name = 'shop/password_reset_email.html'
            message = render_to_string(email_template_name, context)
            send_mail(subject, '', settings.EMAIL_HOST_USER, [email], html_message=message)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Aucun utilisateur trouvé avec cette adresse e-mail.')
            return redirect('password_reset')
        

from django.http import JsonResponse

def get_cart_data(request):
    panier = {} 
    return JsonResponse(panier)
