from django.contrib import admin
from .models import  Trivia_game

class Trivia_admin(admin.ModelAdmin):
    list_display = (
                    'player',
                    'category',
                    'successes',
                    'time'
                    )
    

admin.site.register(Trivia_game, Trivia_admin)
