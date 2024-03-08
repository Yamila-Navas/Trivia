from .models import Trivia
from .forms import Trivia_form
from django.shortcuts import redirect, render
from .trivia_api import obtener_preguntas, parsear_json_preguntas
import json



def inicio(req):
    '''
    esta vista muestra un formulario en la página inicial (index.html),
    procesa los datos del formulario cuando se envía y redirige a otra 
    vista en función de la categoría seleccionada en el formulario.
    '''
    if req.method == 'POST':
        form = Trivia_form(req.POST)
        if form.is_valid():
            partida = form.save(commit=False)

            categoria = partida.categoria

            json_data = obtener_preguntas(categoria)
            
            try:
                # Extraigo el contenido de la respuesta JsonResponse y lo convierto en un diccionario:
                data = json_data.content.decode('utf-8')
                partida.data_api = json.loads(data)
                partida.save()

                return redirect('correr_preguntas', trivia_id=partida.id )
            
            except json.JSONDecodeError as e:
                error_message = f'Error al serializar datos JSON: {str(e)}'
                print(error_message)

                return redirect('error')                
                
    else:
        form = Trivia_form()
        
    return render(req, 'index.html', {'form':form})




def correr_preguntas(req, trivia_id):
    '''
    esta vista se encarga de manejar el flujo de preguntas y respuestas 
    dentro de una partida de trivia, presentando las preguntas al usuario 
    una por una.
    Si ya se han contestado todas las preguntas (9 preguntas), se obtienen 
    las 6 mejores partidas de la misma categoría y se renderiza la plantilla 
    resultados.html para mostrar los resultados finales de la partida, 
    incluyendo los aciertos del usuario y las mejores partidas de la misma categoría. 
    Si la partida del usuario está entre las mejores, se marca con una etiqueta 
    de "record".
    '''
    
    partida = Trivia.objects.get(id=trivia_id)
    numero_pregunta = partida.preguntas_contestadas
    
    pregunta, respuestas_incorrectas, respuesta_correcta = parsear_json_preguntas(partida.data_api, numero_pregunta)

    if req.method == 'POST':
        respuesta_seleccionada = req.POST.get('respuesta')
        
        print('-------- mi respuesta fue: ', respuesta_seleccionada)
        print('-------- la respuesta corecta es: ', respuesta_correcta)
        
        if respuesta_seleccionada == respuesta_correcta:
            partida.aciertos += 1
            partida.save()
            
        # Aumento el número de pregunta contestada para la próxima iteración
        numero_pregunta += 1
        partida.preguntas_contestadas += 1
        partida.save()
        
        
    if numero_pregunta < 9:
        pregunta, respuestas_incorrectas, respuesta_correcta = parsear_json_preguntas(partida.data_api, numero_pregunta)

        ctx = {
            'partida': partida,
            'numero_pregunta': numero_pregunta + 1,
            'pregunta': pregunta,
            'respuestas_incorrectas': respuestas_incorrectas,
            'respuesta_correcta': respuesta_correcta
        }
        return render(req, 'preguntas.html', ctx)
    
    else:
        
        mejores_partidas = Trivia.objects.filter(categoria=partida.categoria).order_by('-aciertos')[:6]
        
        ctx = {
            'aciertos': partida.aciertos,
            'partida': partida,
            'mejores_partidas' : mejores_partidas
        }

        if partida in mejores_partidas:
            ctx['record'] = True
            
        
        return render(req, 'resultados.html', ctx)


    
    




    
    
   









    

    




