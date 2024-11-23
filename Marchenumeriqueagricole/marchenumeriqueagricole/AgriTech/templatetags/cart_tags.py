# myapp/templatetags/cart_tags.py
from django import template

register = template.Library()

@register.filter
def get_item(panier, produit_id):
    # Récupère la quantité du produit dans le panier
    return panier.get(produit_id, 0)
