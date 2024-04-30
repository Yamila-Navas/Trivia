from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=200, unique=True) #no podran haver duplicados de nombre
    slug = models.SlugField(max_length=200, unique=True) #el slug es parte de la url
    games = models.PositiveIntegerField(default=0, blank=True, null=True) # modelo para analiticas

    def __str__(self):
        return self.name
    
    def get_games_count(self):
        """
        este es el contador de las partidas realizadas para esta categoria
        """
        self.games = GameCount.objects.filter(category=self).count
        self.save()
        return self.games
    

class GameCount(models.Model):
    '''
    esta clase guardara las jugada de las categorias
    guarda tambien el ip de la persona que visita el sitio
    '''
    category = models.ForeignKey(Category, related_name="category_game_count", on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ip_address}'