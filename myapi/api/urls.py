from django.urls import path
from .views import *

urlpatterns = [
    path ('recette_frigo',recette_frigo),
    path ('type_de_recette', recette_EntreePlatDessert),
    path ('calorie_comparaison', calorie_comparaison),
    path ('liste_ingredient', listeingredient),
    path ('plus_nourrissant', plus_nourrissant),
    path ('alternative',alternative)
]
