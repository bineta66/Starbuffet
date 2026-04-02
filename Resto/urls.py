from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('cours/', views.cours, name='cours'),
    path('traiteurs/', views.liste_traiteurs, name='liste_traiteurs'),
    path('traiteurs/<int:id>/', views.detail_traiteur, name='detail_traiteur'),  
    path('contact/', views.contact, name='contact'),
    path('inscription-traiteur/', views.inscription_traiteur, name='inscription_traiteur'),
     path('traiteurs/ajouter/', views.ajouter_traiteur, name='ajouter_traiteur'),
   
]