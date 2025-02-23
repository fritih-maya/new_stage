from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name_dep = models.CharField(max_length=50)

    def __str__(self):
        return self.name_dep

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
        extra_fields.setdefault('name_user', mail_user.split('@')[0])

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mail_user, password, **extra_fields)

class User(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=50)
    username = None
    mail_user = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=128)

    departement_principal = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="utilisateurs_principaux"
    )

    departments_with_roles = models.ManyToManyField(
        'Department',
        through='UserDepartmentRole',
        related_name="utilisateurs_associes"
    )

    TYPE_CHOICES = [
        ('chef_service', 'Chef de service'),
        ('directeur_general', 'Directeur général'),
        ('employe_simple', 'Employé simple'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='employe_simple')

    objects = UserManager()

    USERNAME_FIELD = 'mail_user'
    REQUIRED_FIELDS = ['name_user']

    def __str__(self):
        return self.name_user

class UserDepartmentRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    ROLE_CHOICES = [
        ('0', '----'),
        ('1', 'select'),
        ('2', 'upload'),
        ('3', 'delete'),
        ('4', 'select + upload'),
        ('5', 'select + delete'),
        ('6', 'upload + delete'),
        ('7', 'select + upload + delete'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='0')

    class Meta:
        unique_together = ('user', 'department')

    def __str__(self):
        return f"{self.user.name_user} - {self.department.name_dep} - {self.get_role_display()}"

class Files(models.Model):
    name_file = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True) 
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_department = models.ForeignKey('Department', on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='uploads/', default='default.pdf')

    def __str__(self):
        return self.name_file
