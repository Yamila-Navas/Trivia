from django.contrib import admin
from .models import Categorias, Trivia

class Trivia_admin(admin.ModelAdmin):
    list_display = ('jugador','categoria', 'tiempo_inicial', 'tiempo_final','aciertos')
    



admin.site.register(Categorias)
admin.site.register(Trivia, Trivia_admin)
