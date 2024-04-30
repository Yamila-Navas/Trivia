from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'slug', 'games')

admin.site.register(Category, CategoryAdmin)

