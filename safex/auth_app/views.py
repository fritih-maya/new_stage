from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Files  
from .forms_file import FilesForm  

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
    """ Page d'accueil avec liste des fichiers """
    fichiers = Files.objects.all()  # Récupère tous les fichiers
    return render(request, 'acceuil.html', {'fichiers': fichiers})


@login_required
def ajouter_fichier(request):
    """ Ajout d'un fichier par l'utilisateur connecté """
    if request.method == "POST":
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.utilisateur = request.user  # Associe le fichier à l'utilisateur connecté
            fichier.save()
            messages.success(request, "Fichier ajouté avec succès !")
            return redirect('acceuil')  
    else:
        form = FilesForm()
    
    return render(request, 'ajouter_fichier.html', {'form': form})


@login_required
def ajouter_autre_fichier(request):
    """ Ajout d'un autre type de fichier """
    if request.method == "POST":
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.utilisateur = request.user  # Associe le fichier à l'utilisateur connecté
            fichier.save()
            messages.success(request, "Autre fichier ajouté avec succès !")
            return redirect('acceuil')
    else:
        form = FilesForm()
    
    return render(request, 'ajouter_autre_fichier.html', {'form': form})


@login_required
def deconnexion(request):
    """ Déconnexion de l'utilisateur """
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connexion')
