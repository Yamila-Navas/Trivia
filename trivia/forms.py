from django import forms
from .models import Trivia

class Trivia_form(forms.ModelForm):
    class Meta:
        model = Trivia
        exclude = ('tiempo_inicial','tiempo_final','aciertos', 'data_api', 'preguntas_contestadas')
