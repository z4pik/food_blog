from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
# Register your models here.


class RecipeInLine(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "category", "created_at", "id"]
    inlines = [RecipeInLine]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

