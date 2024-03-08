from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=100, blank=False, null=False)
    url_api = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.categoria
    

class Trivia(models.Model):
    jugador = models.CharField(max_length=20, blank=False, null=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    tiempo_inicial = models.DateTimeField(auto_now_add=True)
    tiempo_final = models.DateTimeField(null=True, blank=True)
    aciertos = models.PositiveIntegerField(default=0)
    preguntas_contestadas = models.IntegerField(default=0)
    data_api = models.JSONField(default=None)

    def __str__(self):
        return self.jugador

