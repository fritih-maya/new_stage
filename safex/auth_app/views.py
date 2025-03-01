from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Files, Department  
from .forms_file import FilesForm  

User = get_user_model()

def connexion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(mail_user=email)  # Vérifie l'email
        except User.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")
            return render(request, 'connexion.html')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')  
        else:
            messages.error(request, "Mot de passe incorrect.")

    return render(request, 'connexion.html')


@login_required
def acceuil(request):
    """ Page d'accueil avec liste des fichiers selon le rôle de l'utilisateur """
    user = request.user  
    fichiers = Files.objects.none()  

    department_roles = user.get_department_roles() if hasattr(user, 'get_department_roles') else {}

    print("Roles dict :", department_roles)  

    if not isinstance(department_roles, dict):
        department_roles = {}  

    print("Roles dict pour", user.username, ":", department_roles)
    
    # Départements où l'utilisateur peut voir les fichiers
    authorized_departments = [dep for dep, role in department_roles.items() if role in ['1', '4', '5', '7']]
    
    # Départements où l'utilisateur peut ajouter un fichier
    departments_allowed = Department.objects.filter(id_department__in=[
    int(dep) for dep, role in department_roles.items() if role in ['2', '4', '6', '7']
    ])

    if authorized_departments:
        fichiers = Files.objects.filter(id_department__in=authorized_departments)

    print("Départements autorisés :", authorized_departments)
    print("Départements où ajout autorisé :", departments_allowed)

    return render(request, 'acceuil.html', {
        'fichiers': fichiers,
        'roles_dict': department_roles,
        'departments_allowed': departments_allowed,  # 🔥 Variable pour le template
    })


@login_required
def ajouter_fichier(request):
    """ Ajout d'un fichier par l'utilisateur connecté """
    if request.method == "POST":
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.id_user = request.user  

            # Vérifier si un département a été sélectionné
            department_id = request.GET.get("department")
            if department_id:
                try:
                    fichier.id_department = Department.objects.get(id_department=department_id)
                except Department.DoesNotExist:
                    messages.error(request, "Département invalide.")
                    return redirect('ajouter_fichier')
            else:
                # Assigner automatiquement le département principal si non choisi
                if request.user.departement_principal:
                    fichier.id_department = request.user.departement_principal  
                else:
                    messages.error(request, "Vous devez avoir un département principal ou en sélectionner un.")
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
    fichier = get_object_or_404(Files, id=fichier_id)
    user_roles = request.user.get_department_roles()

    # Vérifier que user_roles est bien un dictionnaire
    if not isinstance(user_roles, dict):
        user_roles = {}

    # Vérifier si l'utilisateur a la permission de supprimer le fichier
    if fichier.id_department.pk in user_roles and user_roles[fichier.id_department.pk] in ['3', '5', '6', '7']:
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
