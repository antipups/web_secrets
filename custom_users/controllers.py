from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from custom_users.forms import LoginForm, RegisterForm
from custom_users.models import MyUser
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout


def auth(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            user = authenticate(request,
                                username=form.cleaned_data['login'],
                                password=form.cleaned_data['public_key'])
            if user:
                login(request, user)

            return redirect('file_storage:file_list')

    else:
        form = LoginForm()

    return render(request, 'custom_users/login.html', {'form': form})


def logout(request: WSGIRequest):
    django_logout(request)
    return redirect('custom_users:auth')
