from rest_framework.decorators import api_view
from rest_framework.response import Response

from .open_ai_service import open_ia_response






@api_view(['POST'])
def recette_frigo(request):
    '''
    Fonctionnalité qui permet d'établir des idées de recette 
    avec aux maximums 5 ingédients que nous
    disposons dans notre frigo
    '''
    prompt = 'Donne moi une liste de recette avec: '
    ingredient1=request.data.get('ingredient1')
    ingredient2=request.data.get('ingredient2')
    ingredient3=request.data.get('ingredient3')
    ingredient4=request.data.get('ingredient4')
    ingredient5=request.data.get('ingredient5')
    if (len(ingredient1)) > 0:
        prompt += ingredient1 + ', '
    if (len(ingredient2)) > 0:
        prompt += ingredient2 + ', '
    if (len(ingredient3)) > 0:
        prompt += ingredient3 + ', '
    if (len(ingredient4)) > 0:
        prompt += ingredient4 + ', '
    if (len(ingredient5)) > 0:
        prompt += ingredient5 + '. '
    return Response(open_ia_response(prompt))
'''
liste d'ingrédient exemple
{
    "ingredient1" : "lait",
    "ingredient2" : "tomate",
    "ingredient3" : "",
    "ingredient4" : "petit pois",
    "ingredient5" : "gorgonzola"

}
'''
@api_view(['POST'])
def recette_EntreePlatDessert(request):
    '''
    Fonctionnalité qui reprend recette_frigo mais
    qui permet de choisir si on cherche une entrée,
    un plat ou un dessert
    '''
    typerecette=request.data.get('typerecette')
    prompt = f"Donne moi une liste de recette pour faire {typerecette}"
    ingredient1=request.data.get('ingredient1')
    ingredient2=request.data.get('ingredient2')
    ingredient3=request.data.get('ingredient3')
    ingredient4=request.data.get('ingredient4')
    ingredient5=request.data.get('ingredient5')
    if (len(ingredient1)) > 0:
        prompt += ingredient1 + ', '
    if (len(ingredient2)) > 0:
        prompt += ingredient2 + ', '
    if (len(ingredient3)) > 0:
        prompt += ingredient3 + ', '
    if (len(ingredient4)) > 0:
        prompt += ingredient4 + ', '
    if (len(ingredient5)) > 0:
        prompt += ingredient5 + '. '
    return Response(open_ia_response(prompt))
'''
liste d'ingrédient exemple pour un dessert
{
    "typerecette": "dessert",
    "ingredient1" : "lait",
    "ingredient2" : "fraise",
    "ingredient3" : "",
    "ingredient4" : "ananas",
    "ingredient5" : "pépite de chocolat"

}
'''

@api_view(['POST'])
def calorie_comparaison(request):
    '''
    Fonctionnalité qui compare les calories entre deux 
    aliments
    '''
    ingredient1=request.data.get('ingredient1')
    ingredient2=request.data.get('ingredient2')
    prompt = f"Fait la comparaison de calorie entre {ingredient1} et {ingredient2} ?"
    return Response(open_ia_response(prompt))   
'''
Exemple avec deux ingrédients
{
    "ingredient1" : "Pépito",
    "ingredient2" : "Oreo"
}
'''

@api_view(['POST'])
def listeingredient(request):
    '''
    Fonctionnalité qui fournit une liste de tous 
    les ingrédients pour une recette
    '''
    recette= request.data.get('recette')
    prompt = f"Donne moi une liste de tous les ingrédients pour la recette {recette}"
    return Response(open_ia_response(prompt))

@api_view(['GET'])

def plus_nourrissant(request):
    '''
    Fonctionnalité qui renvoie le plus nourrissant entre deux aliments
    '''
    a= request.GET.get('a')
    b= request.GET.get('b')
    prompt = f"Quel est l'ingrédient le plus nourrissant entre {a} et {b}?"
    return Response(open_ia_response(prompt))

@api_view(['GET'])

def alternative(request):
    '''
    Fonctionnalité qui renvoie une alternative pour un aliment
    '''
    ingredient= request.GET.get('ingredient')
    prompt = f"Quelle alternative pour {ingredient} exist-il?"
    return Response(open_ia_response(prompt))


    