from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="accueil"),
    path('eleve/delete/<int:id>/', views.supprimer, name='supprimer'),
    path('eleve/edit/<int:id>/', views.modifier, name='modifier'),
]