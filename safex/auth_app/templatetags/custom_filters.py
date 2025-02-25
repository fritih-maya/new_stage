from django import template
register = template.Library()

@register.filter
def to_list(value):
    return value.split(",")  # Transforme "2,4,6,7" en ['2', '4', '6', '7']

@register.filter
def get_item(dictionary, key):
    """ Récupère la valeur d'un dictionnaire à partir d'une clé """
    return dictionary.get(key, '0')  # Retourne '0' si la clé n'existe pas
