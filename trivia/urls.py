from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    
    path('<int:trivia_id>/', views.correr_preguntas, name='correr_preguntas'),
    
]
