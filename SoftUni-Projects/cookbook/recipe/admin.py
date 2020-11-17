from django.contrib import admin
from .models import Recipe, Ingredient


class IngredientInLine(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInLine,
    ]


admin.site.register(Recipe, RecipeAdmin)
