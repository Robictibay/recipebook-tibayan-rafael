from django.contrib import admin
# Import Profile here
from .models import Recipe, Ingredient, RecipeIngredient, Profile 

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]

admin.site.register(Ingredient)
# Register Profile so it shows up in the admin dashboard
admin.site.register(Profile)