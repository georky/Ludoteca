from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

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

#def enviarNotifi(request, telefono, nombreC, nombreR):
    #curso = Curso.objects.get(codigo=codigo)
    #curso.delete()
    #mensaje= 'Estimado '+nombreR+' esta a 5 minutos que se le termine el tiempo de '+nombreC
    #w.sendwhatmsg('+593'+telefono, mensaje, 23, 19,  15, True, 5)
    
  
    
# Create your views here.







# Create your views here.
