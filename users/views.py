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
