from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Partida

# Create your views here.

def home(request):
    return render(request, 'chessapp/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Autentica al usuario con el email y contraseña ingresados
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)  # Inicia sesión en Django
            messages.success(request, 'Inicio de sesión exitoso!')
            return redirect('menu')  # Redirige al menú después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas')  # Mensaje de error si falla el login
            return render(request, 'chessapp/login.html')

    return render(request, 'chessapp/login.html')

def finalizar_partida(request):
    if request.method == 'POST':
        resultado = request.POST.get('resultado')  # Obtener el resultado de la partida
        movimientos = request.POST.get('movimientos')  # Obtener los movimientos
        partida = Partida(jugador=request.user, resultado=resultado, movimientos=movimientos)
        partida.save()  # Guardar la partida en la base de datos
        return redirect('perfil')  # Redirigir al perfil del usuario    

def logout_view(request):
    logout(request)  
    return redirect('home') 

def signin(request):
    return render(request, 'chessapp/signin.html')

def menu(request):
    return render(request, 'chessapp/menu.html')

def tablero(request):
    return render(request, 'chessapp/tablero.html')

def partidas_en_vivo(request):
    return render(request, 'chessapp/partidas_en_vivo.html') 

def tutoriales(request):
    return render(request, 'chessapp/tutoriales.html')
    
def estadisticas_view(request):
    return render(request, 'chessapp/estadisticas.html')

def contacto(request):
    return render(request, 'chessapp/contacto.html')

def configuracion(request):
    return render(request, 'chessapp/configuracion.html')

@login_required  # Este decorador asegura que solo usuarios autenticados puedan acceder a esta vista
def perfil(request):
    partidas = Partida.objects.filter(jugador=request.user)  # Obtener partidas del usuario

    context = {
        'partidas': partidas,
        'usuario': request.user,  # Pasamos el usuario actual al contexto
    }
    return render(request, 'perfil.html', context)
 






