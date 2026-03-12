from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


def validate_short_bio(value: str) -> None:
    if len(value.strip()) <= 255:
        raise ValidationError("short_bio must be more than 255 characters.")


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[validate_short_bio])

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient-detail", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    # Lab 3 fields - Strict mode
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe",
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )

    def __str__(self):
        return f"{self.quantity} {self.ingredient} for {self.recipe}"
    
class RecipeImage(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="recipe_images/")
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description