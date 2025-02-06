from django.db import models

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)   
    name_dep = models.CharField(max_length=50)  

    def __str__(self):
        return self.name_dep  # Pour afficher le nom du département dans l'admin Django

class User(models.Model):
    id_user = models.AutoField(primary_key=True) 
    name_user = models.CharField(max_length=50)  
    mail_user = models.EmailField(unique=True, max_length=50)  # EmailField au lieu de CharField
    psw_user = models.CharField(max_length=50)  
    id_dep = models.ForeignKey(Department, on_delete=models.CASCADE)  # Clé étrangère correcte
    type = models.CharField(max_length=50)       
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name_user  # Affiche le nom dans l'admin Django

class Files(models.Model):
    name_file = models.CharField(max_length=50)  
    date = models.DateField(auto_now_add=True)  # Auto-ajouter la date lors de la création
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Clé étrangère vers User  
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Clé étrangère correcte  

    def __str__(self):
        return self.name_file  # Affiche le nom du fichier dans l'admin Django
