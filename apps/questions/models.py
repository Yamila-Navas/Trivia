from django.db import models
from apps.category.models import Category


class Question(models.Model):

    ask = models.CharField(max_length=300, unique=True)
    option_one = models.CharField(max_length=500)
    option_two = models.CharField(max_length=500)
    option_three = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    registered = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    


    def __str__(self):
        return self.ask
    
 
    
    