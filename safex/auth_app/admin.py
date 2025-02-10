from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import Department
from .models import Files
from .forms import CustomUserChangeForm

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

class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm

    add_fieldsets = (
        ("Informations de connexion", {
            'classes': ('wide',),
            'fields': ('mail_user', 'password1', 'password2'),
        }),
        ("Informations personnelles", {
            'classes': ('wide',),
            'fields': ('name_user', 'id_dep', 'type', 'role'),
        }),
    )

    fieldsets = (
        ("Informations de connexion", {'fields': ('mail_user', 'password')}),
        ("Informations personnelles", {'fields': ('name_user', 'id_dep', 'type', 'role')}),
    )

    list_display = ('mail_user', 'name_user', 'get_departments', 'type', 'role')

    def get_departments(self, obj):
        """ Affiche le département dans l'admin Django """
        return obj.id_dep.name_dep if obj.id_dep else "Aucun"

    get_departments.short_description = 'Départements'

    search_fields = ('mail_user', 'name_user')
    ordering = ('mail_user',)

    raw_id_fields = ('id_dep',)  # ✅ Utilisation correcte pour ForeignKey

safex.register(User, CustomUserAdmin)

