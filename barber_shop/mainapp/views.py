from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, RegistrationForm
from .models import Master, Service


def index_controller(request):
    return render(request, "mainapp/index.html")


def services_controller(request):
    services = Service.objects.all()
    return render(request, "mainapp/services.html", {'services': services})


def masters_controller(request):
    masters = Master.objects.all()
    return render(request, "mainapp/masters.html", {'masters': masters})


def master_controller(request, master_id):
    master = Master.objects.get(pk=master_id)
    return render(request, "mainapp/master.html", {'master': master})


def login_controller(request):
    if request.method != 'POST':
        form = LoginForm()
        return render(request, "mainapp/login.html", {'form': form})

    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, "mainapp/login.html", {'form': form})

    username = form.cleaned_data.get('login')
    password = form.cleaned_data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('services'))

    form.add_error(None, 'Неверный логин или пароль')
    return render(request, "mainapp/login.html", {'form': form})


def logout_controller(request):
    logout(request)
    return redirect(reverse('index'))


def register_controller(request):
    if request.method != 'POST':
        form = RegistrationForm()
        return render(request, "mainapp/registration.html", {'form': form})

    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return render(request, "mainapp/registration.html", {'form': form})

    User.objects.create_user(username=form.cleaned_data.get('login'), password=form.cleaned_data.get('password'))
    return redirect(reverse('login'))
