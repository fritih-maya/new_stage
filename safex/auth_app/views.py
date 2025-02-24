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
    """ Page d'accueil avec liste des fichiers selon le rôle de l'utilisateur """

    user = request.user  
    fichiers = Files.objects.none()  # Par défaut, aucun fichier

    # Récupère les rôles de l'utilisateur dans chaque département
    department_roles = user.get_department_roles()
    
    # Liste des départements où l'utilisateur peut au moins "sélectionner"
    authorized_departments = [dep_id for dep_id, role in department_roles.items() if role in ['1', '4', '5', '7']]

    # Récupère les fichiers des départements autorisés
    if authorized_departments:
        fichiers = Files.objects.filter(id_department__in=authorized_departments)

    return render(request, 'acceuil.html', {'fichiers': fichiers, 'roles': department_roles})



@login_required
def ajouter_fichier(request):
    """ Ajout d'un fichier par l'utilisateur connecté """
    if request.method == "POST":
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.id_user = request.user  # ✅ Associe l'utilisateur

            # ✅ Assigne automatiquement le département principal de l'utilisateur
            if request.user.departement_principal:
                fichier.id_department = request.user.departement_principal  
            else:
                messages.error(request, "Vous devez avoir un département principal.")
                return redirect('ajouter_fichier')

            fichier.save()
            messages.success(request, "Fichier ajouté avec succès !")
            return redirect('acceuil')  
    else:
        form = FilesForm()
    
    return render(request, 'ajouter_fichier.html', {'form': form})

@login_required
def supprimer_fichier(request, fichier_id):
    """ Suppression d'un fichier selon le rôle de l'utilisateur """

    fichier = Files.objects.get(id=fichier_id)
    user_roles = request.user.get_department_roles()

    # Vérifie si l'utilisateur a la permission de supprimer dans ce département
    if fichier.id_department.id in user_roles and user_roles[fichier.id_department.id] in ['3', '5', '6', '7']:
        fichier.delete()
        messages.success(request, "Fichier supprimé avec succès !")
    else:
        messages.error(request, "Vous n'avez pas l'autorisation de supprimer ce fichier.")

    return redirect('acceuil')

@login_required
def deconnexion(request):
    """ Déconnexion de l'utilisateur """
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connexion')
