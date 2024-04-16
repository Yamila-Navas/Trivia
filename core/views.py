from django.shortcuts import render
from django.views import View
from apps.category.models import Category


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')