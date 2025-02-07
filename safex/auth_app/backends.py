from django.contrib.auth.backends import ModelBackend
from auth_app.models import User  # Remplace par le bon chemin de ton modèle

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(mail_user=username)  # Recherche par email
        except User.DoesNotExist:
            return None

        if user.check_password(password):  # Vérifier le mot de passe
            return user
        return None
