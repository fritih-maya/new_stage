from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from django.shortcuts import redirect
from auth_app import views
from auth_app.admin import safex
from auth_app .views import ajouter_fichier
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Page d'administration personnalisée
    path('admin/', safex.urls),

    # Routes utilisateur
    path('connexion/', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('ajouter_fichier/', views.ajouter_fichier, name='ajouter_fichier'),
     path('supprimer_fichier/<int:fichier_id>/', views.supprimer_fichier, name='supprimer_fichier'),

    # Redirection de l'URL racine vers la page d'acceuil'
     path('', lambda request: redirect('connexion'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)