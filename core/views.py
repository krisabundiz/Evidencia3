from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    return render(request, 'core/index.html')

def index(request):
    return render(request,'core/index.html')

def elementos(request):
    return render(request,'core/elementos.html')

def generos(request):
    return render(request,'core/generos.html')

def tecnologia(request):
    return render(request,'core/tecnologia.html')

def influencia(request):
    return render(request,'core/influencia.html')

def exit(request):
    logout(request)
    return redirect('home')