from django.contrib import admin
from .models import User
from .models import Department
from .models import Files

class AdminArea(admin.AdminSite):
    index_title ="Administration "
    site_header =" SAFEX ADMIN "
    site_title =" site safex "

safex = AdminArea(name='safex')    


class AdminFiles(admin.ModelAdmin):
    fields = ['name_file','date']

safex.register(Files, AdminFiles)

class AdminDep(admin.ModelAdmin):
    list_display = ['name_dep','id_department'] 
    
safex.register(Department, AdminDep)   

class AdminUser(admin.ModelAdmin):
    list_display = ['name_user','id_user']

safex.register(User, AdminUser)    
