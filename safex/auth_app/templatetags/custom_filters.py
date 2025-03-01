from django import template
register = template.Library()

@register.filter
def to_list(value):
    return value.split(",")  # Transforme "2,4,6,7" en ['2', '4', '6', '7']

@register.filter
def get_item(dictionary, key):
    """ Récupère la valeur d'un dictionnaire à partir d'une clé """
    return dictionary.get(key, '0')  # Retourne '0' si la clé n'existe pas

@register.filter
def is_in_list(value, arg):
    """ Vérifie si 'value' est dans la liste 'arg' (chaîne séparée par des virgules) """
    allowed_roles = arg.split(",")  # Convertit "2,4,6,7" en ['2', '4', '6', '7']
    return str(value) in allowed_roles  # Compare en tant que chaînes pour éviter les erreurs
