from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# Create your views here.


def index(request):
    return render(request, 'index_2.html')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'paginas_usuario/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'paginas_usuario/login.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrectos.'})
        else:
            login(request, user)
            return render(request, 'index_2.html')


# def register(request):
#     if request.method == 'GET':
#         return render(request, 'paginas_usuario/register.html',
#                       {'form': UserCreationForm})
#     else:
#         print(request.POST)
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 usuario = Usuario(username=request.POST['username'], password=request.POST['password1'])
#                 usuario.save()
#                 login(request, user)
#                 return render(request, 'index_2.html', {'usuario': usuario})
#             except IntegrityError:
#                 return render(request, 'paginas_usuario/register.html',
#                               {'form': UserCreationForm, 'error': 'El usuario ya existe.'})
#     return render(request, 'paginas_usuario/register.html',
#                   {'form': UserCreationForm, 'error': 'Contraseñas no coinciden.'})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def crear(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'paginas_usuario/crear.html', {'formulario': formulario})


def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'paginas_usuario/index.html', {'usuarios': usuarios})


def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None,
                             request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'paginas_usuario/editar.html', {'formulario': formulario})


def eliminar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')

def dan_view(request):
    return render(request, 'paginas_usuario/dan.html')

def orang_view(request):
    return render(request, 'paginas_usuario/orang.html')