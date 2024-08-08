from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from .forms import loginForm,RegistroForm
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Iniciando Sesion.")
                    return HttpResponseRedirect('/account/login')
                else:
                    messages.success(request, "Usuario desactivado")
                    return HttpResponseRedirect('/account/login')
            else:
                messages.success(request, "Usuario o contraseña incorrectas")
                return HttpResponseRedirect('/account/login')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')  # redirige a una página de éxito
    else:
        form = RegistroForm()
    return render(request, 'signup.html', {'form': form})
