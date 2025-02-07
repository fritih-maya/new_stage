from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def connexion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Vérifier si un utilisateur existe avec cet email
        try:
            user = User.objects.get(mail_user=email)  # Rechercher l'utilisateur avec mail_user
        except User.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")
            return render(request, 'connexion.html')

        # Authentifier l'utilisateur avec l'email en tant qu'identifiant
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')  # Redirige vers la page d'accueil
        else:
            messages.error(request, "Mot de passe incorrect.")

    return render(request, 'connexion.html')


@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')
