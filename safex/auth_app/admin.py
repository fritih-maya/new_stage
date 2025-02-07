from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import Department
from .models import Files

class AdminArea(admin.AdminSite):
    index_title ="Administration "
    site_header =" SAFEX ADMIN "
    site_title =" site safex "

safex = AdminArea(name='safex')    


class AdminFiles(admin.ModelAdmin):
    fields = ['name_file','date','file_upload']
    exclude = ('id_user',)  # Cache le champ id_user dans l'admin

    def save_model(self, request, obj, form, change):
        if not obj.id_user:  
            obj.id_user = request.user  # Assigner l'utilisateur connecté
        
        if not obj.id_department and request.user.id_dep:  
            obj.id_department = request.user.id_dep  # Récupérer le département de l'utilisateur
        
        obj.save()

safex.register(Files, AdminFiles)

class AdminDep(admin.ModelAdmin):
    list_display = ['name_dep','id_department'] 
    
safex.register(Department, AdminDep)   

class CustomUserAdmin(UserAdmin):
    # Définir les champs qui doivent apparaître dans le formulaire d'ajout
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mail_user', 'password1', 'password2', 'name_user', 'id_dep', 'type', 'role'),
        }),
    )
    
    # Définir les champs qui doivent apparaître dans le formulaire de modification
    fieldsets = (
        (None, {'fields': ('mail_user', 'password', 'name_user', 'id_dep', 'type', 'role')}),
    )

    # Définir les colonnes visibles dans la liste des utilisateurs
    list_display = ('mail_user', 'name_user', 'id_dep', 'type', 'role', 'is_staff', 'is_active')

    # Les champs utilisés pour rechercher dans l'interface d'administration
    search_fields = ('mail_user', 'name_user')

    # Le champ utilisé pour trier dans l'administration
    ordering = ('mail_user',)

safex.register(User, CustomUserAdmin)    
