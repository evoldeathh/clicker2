from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserSerializerDetail
from rest_framework import generics
from .forms import UserForm
from rest_framework.decorators import api_view


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail


def index(request):
    if len(User.objects.filter(id=request.user.id)) != 0:

        core_model = apps.get_model('backend', 'Core')

        cores = core_model.objects.filter(user=request.user)
        core = None
        if len(cores) == 0 and request.user.is_superuser:
            core = core_model(user=request.user)
            core.save()
        else:
            core = cores.last()
        boostsModel = apps.get_model('backend', 'Boost')
        boosts = boostsModel.objects.filter(core=core)
        return render(request, 'index.html', {
            'core': core,
            'boosts': boosts,
        })

    else:
        return redirect('login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})


def user_logout(request):
    logout(request)
    return redirect('login')


def post(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                coreModel = apps.get_model('backend', 'Core')
                core = coreModel(user=user)
                core.save()
                return redirect('index')
            else:
                return render(request, 'registration.html', {'invalid': True, 'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'invalid': False, 'form': form})
