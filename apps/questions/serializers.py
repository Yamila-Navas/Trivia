from rest_framework import serializers
from .models import Question
from apps.category.serializers import CategorySerializer
import random

class QuestionsSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Asegúrate de que este campo sea de solo lectura si no deseas permitir su modificación a través de este serializador
    
    # Campo adicional para el índice de la pregunta
    index = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Question
        fields = [
            'index',
            'ask',
            'options',
            'correct_answer',
            'category',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question_index = 1  # Inicializamos el contador del índice de pregunta
    

    def get_index(self, obj):
        """
        Método para obtener el índice de la pregunta.
        """
        return self.question_index
    

    def get_options(self, obj):
        """
        Método para obtener las opciones de la pregunta como una lista.
        """
        op = [obj.option_one, obj.option_two, obj.option_three]
        random.shuffle(op)

        return op

    
    def to_representation(self, instance):
        """
        Sobrescribe el método to_representation para personalizar la representación de los datos serializados.
        Aquí generamos un diccionario con índices numéricos autoincrementales para cada pregunta.
        """
        representation = super().to_representation(instance)
        index = self.get_index(instance)  # Obtenemos el índice de la pregunta
        
        # Incrementamos el índice para la próxima pregunta
        self.question_index += 1

        # Actualizamos el valor del índice en la representación
        representation['index'] = index

        return representation
    
    



class ListQuestionsSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) # Asegúrate de que este campo sea de solo lectura si no deseas permitir su modificación a través de este serializador

    class Meta:
        model = Question
        fields = [
            'id',
            'ask',
            'option_one',
            'option_two',
            'option_three',
            'correct_answer',
            'category',
        ]

