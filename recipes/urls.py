
from django.urls import path
from . import views
app_name = 'recipes'
urlpatterns = [
    path('', views.home), #home
    path('', views.home, name='home'),
 # Página inicial
    path('search/', views.search, name="search"),  # Busca
    path('recipes/<int:id>/', views.recipe_detail, name="detail"),
]