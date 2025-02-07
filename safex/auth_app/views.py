from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Enregistrement du nouvel utilisateur
            login(request, user)  # Connexion automatique de l'utilisateur après l'inscription
            return redirect('acceuil')  # Redirection vers la page d'accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

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

        # Authentifier l'utilisateur
        user = authenticate(request, username=user.name_user, password=password) 
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