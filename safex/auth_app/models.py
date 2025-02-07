from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)   
    name_dep = models.CharField(max_length=50)  

    def __str__(self):
        return self.name_dep  # Pour afficher le nom du département dans l'admin Django


class UserManager(BaseUserManager):
    def create_user(self, mail_user, password=None, **extra_fields):
        if not mail_user:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_active', True)
        user = self.model(mail_user=self.normalize_email(mail_user), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mail_user, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mail_user, password, **extra_fields)

class User(AbstractUser):  # ✅ Hériter de AbstractUser
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=50)
    mail_user = models.EmailField(unique=True, max_length=50)  # EmailField au lieu de CharField
    password = models.CharField(max_length=128, default='')
    id_dep = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

    objects = UserManager()

    # Définir USERNAME_FIELD pour l'authentification
    USERNAME_FIELD = 'mail_user'  # Utiliser mail_user comme identifiant unique
    REQUIRED_FIELDS = ['name_user']  # Champs obligatoires lors de la création d'un superuser

    def __str__(self):
        return self.name_user  # Affiche le nom dans l'admin Django

class Files(models.Model):
    name_file = models.CharField(max_length=50)
    date = models.DateField()
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Corrigé !
    id_department = models.ForeignKey('Department', on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='uploads/', default='default.pdf')  # Permet d'ajouter un fichier

    def __str__(self):
        return self.name_file  # Affiche le nom du fichier dans l'admin Django
