from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path("recipes/", RecipeListView.as_view(), name="recipe-list"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe-create"),
    path("recipe/<int:pk>/add_image/", RecipeImageCreateView.as_view(), name="recipe-image-create"),
]