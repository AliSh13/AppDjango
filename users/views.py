from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def login_view(request):
    """ Вход """
    if request.method != 'POST':
        form = AuthenticationForm()
        context = {'form': form }
        return render(request, 'users/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = AuthenticationForm()
            messege = 'не верные данные, попробуйте снова.'
            context = {'form': form, 'messege': messege}
            return render(request, 'users/login.html', context)


def logout_view(request):
    """Завершает сеанс работы с приложением"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_view(request):
    """ Регистрация """
    if request.method != 'POST':
        form = UserCreationForm()
        context = {'form': form }
        return render(request, 'users/register.html', context)
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            username = new_user.username
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

    form = UserCreationForm()
    messege = 'Не не подходящие данные, попробуйте снова.'
    context = {'form': form, 'messege': messege}
    return render(request, 'users/register.html', context)
