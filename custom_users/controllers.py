from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from custom_users.forms import LoginForm, RegisterForm


def auth(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return redirect('file_storage:file_list')

    else:
        form = LoginForm()

    return render(request, 'custom_users/login.html', {'form': form})
