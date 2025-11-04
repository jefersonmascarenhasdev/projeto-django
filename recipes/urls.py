
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #home
    path('', views.index, name="recipes-home"),  # Página inicial
    path('search/', views.search, name="recipes-search"),  # Busca
    path('recipes/<int:id>/', views.recipe, name="recipe-detail"),
]