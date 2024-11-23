"""
URL configuration for marchenumeriqueagricole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AgriTech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('product/',views.product,name='product'),
    path('blog/',views.blog,name='blog'),
    path('detail/',views.blog,name='detail'),
    path('feature/',views.feature,name='feature'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.contact,name='service'),
    path('connexion', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('legumes/', views.legumes, name='legumes'),
     path('legumes/', views.legumes, name='legumes'),
    path('fruits/', views.fruits, name='fruits'),
    path('cart/', views.cart, name='cart'),
    path('paiement/', views.paiement, name='paiement'),
    path('liste_produits/', views.liste_produits, name='liste_produits'),
    path('produits/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('produits/modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('add-to-cart/<int:produit_id>/', views.add_to_cart, name='add_to_cart'),
    path('admin/commandes/', views.traiter_commandes, name='traiter_commandes'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)