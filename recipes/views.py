from django.shortcuts import render, get_object_or_404
from .models import Recipe
from utils.recipes.factory import make_recipe




def home(request):
    return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)]
    })


def index(request):
    return render(request, "recipes/pages/index.html")


# Página de busca
def search(request):
    search_term = request.GET.get("q", "")
    context = {
        "search_term": search_term,
    }
    return render(request, "recipes/pages/search.html", context)


# Página de detalhe da receita
def recipe(request, id):
    context = {
        "recipes": make_recipe(),
    }
    return render(request, "recipes/pages/recipe-view.html", context)
def recipe_detail(request, id):
    recipe = make_recipe()
    recipe['id'] = id  # só pra manter coerência na URL
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True,
    })