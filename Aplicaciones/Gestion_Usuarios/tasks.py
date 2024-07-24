

from urllib import request
from celery import shared_task
import http.client
from django.shortcuts import redirect
import request2
import json
import jsonify
from django.contrib import messages

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
def task_periodic(request,bind= True):
    #texto = texto.lower()
    
    #mensaje= 'Estimado '+nombreR+' esta a 5 minutos que se le termine el tiempo de '+nombreC
    
    data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": '593979418199',
            "type": "text",
            "text": {
                "preview_url": False,
                "body": 'mensaje'
            }
    }
  #Convertir el diccionaria a formato JSON
    data=json.dumps(data)

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer EAAOyRshDbC8BOz2bvkJI922HNuXYGgEUtknT4Ajhog5AUAIHg1XzWZCp1ywehhKTPE1mW1upmF8cW0G7Oc8iuza0VPimg7ZCkZBRatCAQakFnscP99o2vH3BPDZCACZAhNIIsblajrlDXszb8jsXilmM25yupCCbZB6rjapXZClvYePtveFPdqI15LTf0ZCFSSU6"
    }

    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST","/v19.0/346378921896150/messages", data, headers)
        response = connection.getresponse()
        print("Tarea periódica ejecutada.")
        #print(response.status, response.reason)
       # messages.success(request, '¡Mensaje Enviado!')
       # return redirect('/')
    except Exception as e:
        print(str(e))
    finally:
       connection.close()
    
    #return 'Done'
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