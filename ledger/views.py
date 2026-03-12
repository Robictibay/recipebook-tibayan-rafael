from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage 

class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "ledger/recipe_form.html"
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "ledger/recipe_image_form.html"
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.kwargs['pk']})