

from urllib import request
from celery import shared_task
import http.client
from django.shortcuts import redirect
import request2
import json
import jsonify
from django.contrib import messages
from .models import Usuario


@shared_task(bind=True)
def test_func0(bind= True):
    for i in range(10):
        print(i)
    return 'Done'

@shared_task()
def mul(a,b):
    return a * b
TOKEN_ANDERCODE = "ANDERCODE"

def webhook():
    if request2.method == 'GET':
        challenge = verificar_token(request2)
        return challenge
    elif request2.method == 'POST':
        reponse = recibir_mensajes(request2)
        return reponse

def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')

    if challenge and token == TOKEN_ANDERCODE:
        return challenge
    else:
        return jsonify({'error':'Token Invalido'}),401
@shared_task(bind=True)
def task_periodic(request,bind=True):
    # Filtrar usuarios con campo3 igual a 'PENDIENTE'
    usuariosListados = Usuario.objects.filter(campo3='PENDIENTE')
    
    # Iterar sobre los usuarios filtrados
    for usuario in usuariosListados:
        telefono = usuario.telefono
        mensaje = usuario.mensaje
        # Preparar el payload para enviar el mensaje a WhatsApp
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": '593'+telefono,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": mensaje  # Aquí debes colocar el mensaje que deseas enviar
            }
        }
        
        # Convertir el diccionario a formato JSON
        data_json = json.dumps(data)
        
        # Configurar los headers para la solicitud HTTP
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer EAAOyRshDbC8BOz2bvkJI922HNuXYGgEUtknT4Ajhog5AUAIHg1XzWZCp1ywehhKTPE1mW1upmF8cW0G7Oc8iuza0VPimg7ZCkZBRatCAQakFnscP99o2vH3BPDZCACZAhNIIsblajrlDXszb8jsXilmM25yupCCbZB6rjapXZClvYePtveFPdqI15LTf0ZCFSSU6"
        }
        
        # Realizar la conexión HTTPS con la API de WhatsApp de Facebook
        try:
            connection = http.client.HTTPSConnection("graph.facebook.com")
            connection.request("POST", "/v19.0/346378921896150/messages", data_json, headers)
            
            response = connection.getresponse()
            print(f"Mensaje enviado a {telefono}. Estado: {response.status}, Razón: {response.reason}")
            
            # Aquí puedes manejar la respuesta si es necesario
            # Por ejemplo, verificar response.status para asegurarte de que el mensaje se haya enviado correctamente.
            
        except Exception as e:
            print(f"Error al enviar mensaje a {telefono}: {str(e)}")
            
        finally:
            connection.close()
             
def recibir_mensajes(req):
    try:
        req = request2.get_json()
        entry =req['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        objeto_mensaje = value['messages']

      #return jsonify({'message':'EVENT_RECEIVED'})
    except Exception as e:
      return jsonify({'message':'EVENT_RECEIVED'})
  