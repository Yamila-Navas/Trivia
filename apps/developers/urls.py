from django.urls import path
from .views import *

urlpatterns = [
    path("generate-url/", GenerateUrlApiView.as_view(), name="generate-url")
]
