from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from django.shortcuts import redirect
from auth_app import views
from auth_app.admin import safex

urlpatterns = [
    # Page d'administration personnalisée
    path('admin/', safex.urls),

    # Routes utilisateur
    path('connexion/', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    # Redirection de l'URL racine vers la page de connexion
    path('', lambda request: redirect('connexion')),
]
