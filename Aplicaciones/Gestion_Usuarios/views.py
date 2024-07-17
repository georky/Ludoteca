from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
import http.client
import request2
import json
import jsonify
# Create your views here.


def home(request):
    usuariosListados = Usuario.objects.all()
    messages.success(request, 'Usuarios listados!')
    return render(request, "gestionUsuarios.html", {"usuarios": usuariosListados})


def registrarUsuarios(request):
    telefono = request.POST['txtTelefono']
    nombreC = request.POST['txNombreC']
    nombreR = request.POST['txtNombreR']
    tiempoH = request.POST['numHoras']
    usuario = Usuario.objects.create(
        telefono=telefono, nombreC=nombreC,nombreR=nombreR, tiempoH=tiempoH)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')

def edicionUsuario(request, telefono):
    usuario = Usuario.objects.get(telefono=telefono)
    return render(request, "edicionUsuarios.html", {"usuario": usuario})

def editarUsuario(request):
    telefono = request.POST['txtTelefono']
    nombreC = request.POST['txNombreC']
    nombreR = request.POST['txtNombreR']
    tiempoH = request.POST['numHoras']

    usuario = Usuario.objects.get(telefono=telefono)
    usuario.nombreC = telefono
    usuario.nombreC = nombreC
    usuario.nombreR = nombreR
    usuario.tiempoH = tiempoH
    usuario.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')

def eliminarUsuarios(request, telefono):
    usuario = Usuario.objects.get(telefono=telefono)
    usuario.delete()

    messages.success(request, '¡Curso eliminado!')
    return redirect('/')
#Token de verificacion para la configuracion
TOKEN_ANDERCODE = "ANDERCODE"

#@app.route('/webhook', methods=['GET','POST'])
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
def enviarNotifi(texto, telefono, nombreC, nombreR):
    #texto = texto.lower()
    
    mensaje= 'Estimado '+nombreR+' esta a 5 minutos que se le termine el tiempo de '+nombreC
    
    data={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": '593979418199',
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, ¿Cómo estás? Bienvenido."
            }
    }
  #Convertir el diccionaria a formato JSON
    data=json.dumps(data)

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer EAAOyRshDbC8BOZCUrC5usRMvAQflWRerrLz2pxYaREaO2udlYsa4tfMZBChlkl1W6ZAMEklnY50bDt40YSQYCWhZByr7x6JzCOsrILZBqw0Rw20DfpbIIphjXptXF1iUAWbRBpZBxZCZC7iel2VYXVvdIxbCcZA5IUJVn001xkAbGRSgpZBhYAVHTdvVFiGNeGXdZCQ"
    }

    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST","/v19.0/346378921896150/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
        return redirect('/')
    except Exception as e:
        print(json.dumps(e))
    finally:
        connection.close()
    
# Create your views here.
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





# Create your views here.
