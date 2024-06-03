from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #Manejo de sesion de django
from django.contrib import messages

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login efectivo: '+' '+ username)
        else:
            messages.info(request, 'Credenciales no válidas.')

    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')
