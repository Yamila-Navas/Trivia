from django.urls import path
from .views import *

urlpatterns = [

    path('', StartGameView.as_view(), name='start-game'),
    path('results-game/<int:game_id>/', ResultsGameView.as_view(), name='results-game'),
    

    path('df/', crear_df, name='crear_df'),
    
]
