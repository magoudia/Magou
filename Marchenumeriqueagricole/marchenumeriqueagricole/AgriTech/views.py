from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Produit
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Produit, Feedback

# Create your views here.


def about(request):
    return render(request, 'about.html')

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

def index(request):
    return render(request, 'index.html')


def legumes(request):
    produits = Produit.objects.all()
    for produit in produits:
        if not produit.image or not produit.image.name:
            produit.image = None  # Ou utilisez une image par défaut
    return render(request, 'legumes.html', {'produits': produits})

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