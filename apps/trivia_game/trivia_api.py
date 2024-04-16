from django.http import JsonResponse
import requests
import json


def obtener_preguntas(categoria):
    '''
    esta función intenta obtener datos de una API externa utilizando 
    la URL especificada en el atributo url_api de la categoría proporcionada 
    y devuelve los datos obtenidos o un mensaje de error en formato JSON, 
    dependiendo del resultado de la solicitud.
    '''

    try:
        respuesta = requests.get(categoria.url_api)
        if respuesta.status_code == 200:
            data = respuesta.json()
            print(data)
            return JsonResponse(data)
        else:
            status = respuesta.status_code
            return JsonResponse({'error': f'Error en la solicitud: {status}'}, status=status)
    
    except Exception as e:
        return JsonResponse({'error': f'Error en la solicitud: {str(e)}'}, status=500)
    


def parsear_json_preguntas(data, siguiente_pregunta):
    '''
    esta función va a extraer y parsear los datos de una pregunta 
    específica de los datos JSON de la trivia.
    '''

    data_por_pregunta = data['results'][siguiente_pregunta]

    pregunta = data_por_pregunta['question']

    respuestas_incorrectas = data_por_pregunta['incorrect_answers']

    respuesta_correcta = data_por_pregunta['correct_answer']

    return pregunta, respuestas_incorrectas, respuesta_correcta


