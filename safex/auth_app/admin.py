from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Files, UserDepartmentRole
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

### 🔹 Gestion des rôles des utilisateurs par département
class UserDepartmentRoleInline(admin.TabularInline):
    model = UserDepartmentRole
    extra = 1

    def has_add_permission(self, request, obj=None):
        if obj and obj.type == 'employe_simple':
            return False  # Empêche l'ajout de plusieurs départements
        return super().has_add_permission(request, obj)

### 🔹 Gestion des utilisateurs
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    
    list_display = ('mail_user', 'name_user', 'get_departments', 'type', 'is_superuser')
    list_editable = ('type',)
    
    ordering = ('mail_user',)  # ✅ Correction ici pour éviter l'erreur

    add_fieldsets = (
        ("Informations de connexion", {
            'classes': ('wide',),
            'fields': ('mail_user', 'password1', 'password2', 'name_user'),
        }),
        ("Département principal", {
            'classes': ('wide',),
            'fields': ('departement_principal', 'type'),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )
    
    fieldsets = (
        ("Informations de connexion", {'fields': ('mail_user', 'password')}),  
        ("Informations personnelles", {'fields': ('name_user', 'type')}),  
        ("Départements", {'fields': ('departement_principal',)}),  
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser')}),  
    )
    
    inlines = [UserDepartmentRoleInline]
    
    def get_departments(self, obj):
        primary_dep = obj.departement_principal.name_dep if obj.departement_principal else "Aucun"
        secondary_deps = ", ".join([udr.department.name_dep for udr in obj.userdepartmentrole_set.all()])
        return f"{primary_dep} | {secondary_deps}" if secondary_deps else primary_dep

    get_departments.short_description = 'Départements'

    def save_model(self, request, obj, form, change):
        if obj.type == 'employe_simple':
           obj.save()  # ✅ Sauvegarde l'utilisateur avant d'accéder à ManyToMany
           obj.departments_with_roles.clear()  
        UserDepartmentRole.objects.filter(user=obj).delete()  # Supprime les rôles secondaires

        super().save_model(request, obj, form, change)


# Enregistrement des modèles
safex.register(Files, AdminFiles)
safex.register(Department, AdminDep)
safex.register(User, CustomUserAdmin)
safex.register(UserDepartmentRole)
