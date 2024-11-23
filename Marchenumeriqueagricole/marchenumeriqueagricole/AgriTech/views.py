from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Commande, Produit
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Produit, Feedback
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProduitForm


# Create your views here.


def about(request):
    return render(request, 'about.html')


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produits_list')  # Redirige vers la liste des produits après ajout
    else:
        form = ProduitForm()
    
    return render(request, 'ajouter_produit.html', {'form': form})


def service(request):
    return render(request, 'service.html')

def product(request):
    return render(request, 'product.html')

def blog(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def paiement(request):
    # Charger les éléments du panier et le total
    cart_items = request.session.get('cart_items', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'paiement.html', context)

from django.shortcuts import render

def cart(request):
    cart_items = request.session.get('cart', [])
    cart_total = 0

    for item in cart_items:
        # Calcul du total pour chaque produit
        item['total'] = item['product']['price'] * item['quantity']
        cart_total += item['total']

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, produit_id):
    # Logique pour ajouter un produit au panier
    # Vous pouvez utiliser la session pour stocker le panier temporairement
    panier = request.session.get('panier', {})
    panier[produit_id] = panier.get(produit_id, 0) + 1
    request.session['panier'] = panier
    return redirect('cart')

def index(request):
    return render(request, 'index.html')


def legumes(request):
    produits = Produit.objects.all()
    for produit in produits:
        if not produit.image or not produit.image.name:
            produit.image = None  # Ou utilisez une image par défaut
    return render(request, 'legumes.html', {'produits': produits})

def fruits(request):
    return render(request, 'fruits.html')

def produits(request):
    produits = Produit.objects.all()  # Récupère tous les produits
    return render(request, 'legumes.html', {'produits': produits})

def connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Rediriger vers la page d'index ou une autre page après connexion
        else:
            # Si l'authentification échoue
            return render(request, 'connexion.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect'})
    
    return render(request, 'connexion.html')


def inscription(request):
  
    if request.method == "POST":
        username = request.POST.get('username')  # Assurez-vous que 'username' est bien récupéré
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Vérifier si le nom d'utilisateur est déjà pris
        if User.objects.filter(username=username).exists():
            return render(request, 'inscription.html', {'error': 'Le nom d\'utilisateur est déjà pris'})

        # Vérifier si l'email est déjà utilisé
        if User.objects.filter(email=email).exists():
            return render(request, 'inscription.html', {'error': 'L\'email est déjà utilisé'})

        try:
            # Créer l'utilisateur avec un nom d'utilisateur, un email et un mot de passe
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('connexion')  # Rediriger vers la page de connexion après l'inscription
        except IntegrityError:
            return render(request, 'inscription.html', {'error': 'Une erreur s\'est produite lors de l\'inscription'})

    return render(request, 'inscription.html')

# Afficher la liste des produits
def liste_produits(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'liste_produits.html', {'produits': produits})

# Supprimer un produit
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    messages.success(request, f'Le produit "{produit.nom}" a été supprimé avec succès!')
    return redirect('liste_produits')

# Modifier un produit
def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.nom = request.POST.get('nom')
        produit.description = request.POST.get('description')
        produit.prix = request.POST.get('prix')
        produit.categorie = request.POST.get('categorie')
        produit.save()
        messages.success(request, f'Le produit "{produit.nom}" a été modifié avec succès!')
        return redirect('liste_produits')
    return render(request, 'modifier_produit.html', {'produit': produit})

def traiter_commandes(request):
    commandes = Commande.objects.all().order_by('-date_commande')

    if request.method == "POST":
        commande_id = request.POST.get('commande_id')
        nouveau_statut = request.POST.get('statut')
        commande = get_object_or_404(Commande, id=commande_id)
        commande.statut = nouveau_statut
        commande.save()
        return redirect('traiter_commandes')

    context = {
        'commandes': commandes,
    }
    return render(request, 'admin/traiter_commandes.html', context)