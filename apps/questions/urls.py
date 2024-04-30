from django.urls import path
from .views import *

urlpatterns = [
    path("fill-db/", FillDatabaseView.as_view(), name="fill-db"),
    path("list-questions/", ListQuestionsView.as_view(), name="list-questions"),
    path("list/", ListQuestionsByCategoryView.as_view(), name="list-questions"),
    
   path("delete-db/", DeleteView.as_view(), name="delete-db"),
]