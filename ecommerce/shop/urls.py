from django.urls import path
from django.contrib.auth import views as auth_views
from shop.views import index, detail,  logi, register, logOut, MyPasswordResetView, confirm_account, confirm_account_success, confirm_account_failed
from django.urls import reverse
from . import views 
from .views import vos_commandes,  mon_compte,  category_products, contact_form_submit




urlpatterns = [
    path('', index, name='home'),
    path('get_cart_data', views.get_cart_data, name='get_cart_data'),
    path('<int:myid>', detail, name="detail"),
    path('vos-commandes/', vos_commandes, name='vos_commandes'),
    path('mon_compte/', mon_compte, name='mon_compte'),
    
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('contact/', views.contact, name='contact'),
    path('aide/', views.aide, name='aide'),
    path('contact_form_submit/', contact_form_submit, name='contact_form_submit'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('category_products/<str:category_name>/', category_products, name='category_products'),
    path('login',  logi, name='login'),
    path('register', register, name="register"),
    path('confirm/<uidb64>/<token>/', confirm_account, name='confirm_account'),
    path('confirm_account/success/', confirm_account_success, name='confirm_account_success'),
    path('confirm_account/failed/', confirm_account_failed, name='confirm_account_failed'),
    path('logout', logOut, name="logout"),
    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'), name='password_reset_complete'),
    path('laptops/', views.laptops, name='laptops'),
    path('smartphones/', views.smartphones, name='smartphones'),
    path('vehicules/', views.vehicules, name='vehicules'),
    path('panier/', views.panier, name='panier'),
    path('commande/', views.commande, name='commande'),
    path('update_article/', views.update_article, name='update_article'),
    path('traitement-commande/', views.traitementCommande, name="traitement_commande")
]