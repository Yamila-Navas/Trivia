from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apps.category.models import Category
from .models import Question
from apps.category.serializers import CategorySerializer
from .serializers import QuestionsSerializers
from .paginations import *
from .fill_database import fill_database

class FillDatabaseView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        try:
            if fill_database():
                return Response({'message': 'Las preguntas se han cargado con éxito.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No se pudo cargar las preguntas.'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'message': f'Ocurrió un error al cargar las preguntas: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListQuestionsView(APIView):
    '''
    listara tosas las preguntas que existen en la base de datos.
    '''
    permission_classes=(permissions.AllowAny,)

    def get(self, request):
        if Question.objects.all().exists():

            questions = Question.objects.all()
            
            paginator = SmallSetPagination()
            result = paginator.paginate_queryset(questions, request)
            
            serializer = QuestionsSerializers(result, many=True)
            

            return paginator.get_paginated_response({'questions': serializer.data})
        
        else:
            return Response({'questions':'not found'}, status=status.HTTP_404_NOT_FOUND)


class ListQuestionsByCategoryView(APIView):
    '''
    listara las preguntas por categoria y cantidad especificada.
    '''
    permission_classes=(permissions.AllowAny,)

    def get(self, request):
        try:
            if Question.objects.all().exists():
                # recolecto los parametros categoria y cantidad de preguntas
                category_slug = request.query_params.get('category_slug')
                number_of_questions = int(request.query_params.get('number_of_questions'))

                # filtro la db para traer las preguntas relacionadas a la categoria, en forma aliatoria.
                questions = Question.objects.filter(category__slug=category_slug).order_by('?')[:number_of_questions]
                
                # serializo los resultados
                serializer = QuestionsSerializers(questions, many=True)
                
                return Response({'questions': serializer.data}, status=status.HTTP_200_OK)

            else:
                return Response({'questions':'not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'message': f'An error occurred while loading questions: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



