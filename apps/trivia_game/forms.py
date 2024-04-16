from django import forms
from .models import Trivia_game

class Trivia_form(forms.ModelForm):
    class Meta:
        model = Trivia_game
        exclude = (
                    'initial_time',
                    'final_time',
                    'successes',
                    'answered_questions',
                    )
        