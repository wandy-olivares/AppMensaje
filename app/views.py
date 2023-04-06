from django.shortcuts import render
from .models import User, Registros
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    
    registros = Registros()
    registrar_usuario = User()
    comprobar_usuario_registrados = User.objects.all()

    # Llamar todos los usuarios e ingresarlos a una lista, 
    # para verificar que el  usuario exista o no.

    lista_usuarios_registrados = []

    for usuario in comprobar_usuario_registrados:
        lista_usuarios_registrados.append(usuario.nombre)
        

    if request.method == 'POST':
        registrar_usuario.nombre = request.POST['nombre']
        if registrar_usuario.nombre == '':
            print('viene vacio')
        else:
            for usuario in lista_usuarios_registrados:
                if usuario == registrar_usuario.nombre:
                        registros.nombre = registrar_usuario.nombre
                        registros.save()
                        return HttpResponseRedirect('/home/')
                        
                        
                        
    return render(request, 'app/login.html')


def home(request):
    registros = Registros.objects.all()
    nombre = ''
    for user in registros:
        nombre = user.nombre
    
    context = {
        'nombre': nombre,
    }
    return render(request, 'app/home.html', context)