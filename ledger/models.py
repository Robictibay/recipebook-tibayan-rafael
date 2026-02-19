from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient-detail", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe",  # REQUIRED
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",  # REQUIRED
    )

    def __str__(self):
        return f"{self.quantity} {self.ingredient} for {self.recipe}"