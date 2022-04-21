from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView


class FileList(LoginRequiredMixin, ListView):
    ...
