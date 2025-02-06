from django.contrib import admin
from .models import User
from .models import Department
from .models import Files

class AdminArea(admin.AdminSite):
    index_title ="Administration "
    site_header =" SAFEX ADMIN "
    site_title =" site safex "

safex = AdminArea(name='safex')    

safex.register(User)
safex.register(Department)
safex.register(Files)
