from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Files
from .forms import CustomUserChangeForm

class AdminArea(admin.AdminSite):
    index_title = "Administration"
    site_header = "SAFEX ADMIN"
    site_title = "Site SAFEX"

safex = AdminArea(name='safex')    

### 🔹 Gestion des fichiers (Files)
class AdminFiles(admin.ModelAdmin):
    fields = ['name_file', 'date', 'file_upload']
    exclude = ('id_user',)

    def save_model(self, request, obj, form, change):
        if not obj.id_user:  
            obj.id_user = request.user
        
        if not obj.id_department and request.user.departement_principal:  
            obj.id_department = request.user.departement_principal
        
        obj.save()

### 🔹 Gestion des départements
class AdminDep(admin.ModelAdmin):
    list_display = ['id_department', 'name_dep']

### 🔹 Gestion des utilisateurs
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    
    list_display = ('mail_user', 'name_user', 'get_departments', 'type', 'role', 'is_superuser')
    list_editable = ('type', 'role')
    
    # Modification de l'ordre des fieldsets pour la création
    add_fieldsets = (
        ("Informations de connexion", {
            'classes': ('wide',),
            'fields': ('mail_user', 'password1', 'password2', 'name_user'),
        }),
        ("Département principal", {
            'classes': ('wide',),
            'fields': ('departement_principal', 'type', 'role'),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ("Départements secondaires", {
            'classes': ('wide',),
            'fields': ('departements_secondaires',),
        }),
    )
    
    # Fieldsets pour l'édition
    fieldsets = (
        ("Informations de connexion", {'fields': ('mail_user', 'password')}),
        ("Informations personnelles", {'fields': ('name_user', 'type', 'role')}),
        ("Départements", {'fields': ('departement_principal', 'departements_secondaires')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    def get_departments(self, obj):
        primary_dep = obj.departement_principal.name_dep if obj.departement_principal else "Aucun"
        secondary_deps = ", ".join([dep.name_dep for dep in obj.departements_secondaires.all()])
        return f"{primary_dep} | {secondary_deps}" if secondary_deps else primary_dep

    get_departments.short_description = 'Départements'

    def save_model(self, request, obj, form, change):
        if not change:  # Si c'est une création
            # Sauvegarde d'abord l'utilisateur
            super().save_model(request, obj, form, change)
            
            # Si c'est un employé simple, on s'assure qu'il n'a pas de départements secondaires
            if obj.type == 'employe_simple':
                obj.departements_secondaires.clear()
        else:
            super().save_model(request, obj, form, change)

    search_fields = ('mail_user', 'name_user')
    ordering = ('mail_user',)
    raw_id_fields = ('departement_principal',)
    filter_horizontal = ('departements_secondaires',)

# Enregistrement des modèles
safex.register(Files, AdminFiles)
safex.register(Department, AdminDep)
safex.register(User, CustomUserAdmin)