from django.shortcuts import render
from django.views import View
from apps.category.models import Category
from django.conf import settings



class GenerateUrlApiView(View):
    '''
    esta vista muestra un formulario en form_to_generate_url.html,
    procesa los datos del formulario y genera la url para la Api.
    '''
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'form_to_generate_url.html', {'categories':categories})
    
    def post(self, request):
        categories = Category.objects.all()
        category_slug = request.POST.get('category')
        quantity = str(request.POST.get('quantity'))
        
        # recojo el dominio de mi sitio
        domain = settings.DOMAIN

        url = f'{domain}/api/questions/list/?category_slug={category_slug}&number_of_questions={quantity}'
        context = {
            'categories':categories,
            'url' : url
        }

        return render(request, 'form_to_generate_url.html', context)