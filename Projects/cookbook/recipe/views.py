from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def list_recipes(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecipeForm()
    return render(request, 'recipe/list.html', context={
        'recipes': recipes,
        'form': form,
    })


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect('/recipes/')


def view_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe/view.html', context={
        'recipe': recipe,
    })
