from django.db import models
from apps.category.models import Category
    

class Trivia_game(models.Model):
    player = models.CharField(max_length=20, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    initial_time = models.DateTimeField(auto_now_add=True)
    successes = models.PositiveIntegerField(default=0)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.player

