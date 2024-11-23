
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.contrib.auth.models import AbstractUser


# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('agriculteur', 'Agriculteur'),
        ('operateur', 'Opérateur'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    # Ajout de related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changez ce nom selon votre préférence
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changez ce nom selon votre préférence
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
)
# Modèle Agriculteur
class Agriculteur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

# Modèle Opérateur
class Operateur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

# Modèle Produit
class Produit(models.Model):
    CATEGORIES = [
        ('Légume', 'Légume'),
        ('Fruit', 'Fruit'),
        ('Céréale', 'Céréale'),
        # Ajoutez d'autres catégories si nécessaire
    ]
    
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', default='produits/Crêpes_de_courgettes_soufflées.jpg')   # Nécessite Pillow pour gérer les images
    disponible = models.BooleanField(default=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.nom

class Feedback(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()  # Ex. note de 1 à 5

    def __str__(self):
        return f"Feedback de {self.user.username} sur {self.produit.nom}"

# Modèle Commande
class Commande(models.Model):
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('Traitée', 'Traitée'),
        ('Annulée', 'Annulée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through='CommandeProduit')
    
    def default_date():
         return now()

    date_commande = models.DateTimeField(default=default_date) 
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='En attente')

    def __str__(self):
        return f"Commande #{self.id} - {self.utilisateur.username}"

# Modèle Transaction
class Transaction(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return f"Transaction {self.id} - {self.amount} FCFA"

# Modèle Feedback


# Modèle Suivi de Stock
class SuiviDeStock(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()
    alert_threshold = models.IntegerField()

    def __str__(self):
        return f"Suivi de stock pour {self.produit.name}"
    
class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Commande #{self.commande.id})"