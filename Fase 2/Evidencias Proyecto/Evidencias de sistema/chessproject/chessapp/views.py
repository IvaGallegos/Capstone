from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'chessapp/home.html')

def login_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Aquí puedes implementar tu lógica para autenticar con Firebase
        # Si la autenticación es exitosa
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Inicia sesión en Django
            return redirect('menu')  # Redirige al menú después de iniciar sesión
        else:
            return render(request, 'chessapp/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'chessapp/login.html')

def logout_view(request):
    logout(request)  
    return redirect('home') 

def signin(request):
    return render(request, 'chessapp/signin.html')

def menu(request):
    return render(request, 'chessapp/menu.html')

def tablero(request):
    return render(request, 'chessapp/tablero.html')


def home(request):
    return render(request, 'chessapp/home.html')  

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







